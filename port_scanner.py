#!/usr/bin/env python

import argparse
import re
import ast
import socket
import io
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def hostname(name):
  "Validate address"

  try:
    socket.gethostbyname(name)
    return name
  except socket.gaierror:
    raise argparse.ArgumentTypeError("Invalid hostname: " + name)
  try:
    socket.inet_aton(name)
    return name
  except socket.error:
    raise argparse.ArgumentTypeError("Invalid ip address: " + name)

def ports(ports):
  "Validate the ports"

  re_list = re.compile(r"\d+\,\d+")
  re_range = re.compile(r"\d+\:\d+")
  ip_range = range(0, 65535)

  try:
    if int(ports):
      if ports not in ip_range:
        return [ports]
      else:
        raise argparse.ArgumentTypeError("port must be 0-65535")
  except ValueError:
    if re_list.match(ports):
      try:
        return [port for port in ast.literal_eval(ports) if port in ip_range ]
      except:
        raise argparse.ArgumentTypeError("Invalid range: " + ports)
    elif re_range.match(ports):
      start, stop = (int(i) for i in ports.split(":"))
      if start in ip_range and stop in ip_range and stop > start:
        return range(start, stop + 1)
      else:
        raise argparse.ArgumentTypeError("port must be 0-65535 and 2nd ip should be greater than 1st ip")        
    else:
      raise argparse.ArgumentTypeError("Invalid ports: " + ports)


def scan(hostname, ports):
  # Print a nice banner with information on which host we are about to scan
  print "-" * 60
  print "Please wait, scanning host", hostname
  print "-" * 60


  try:
    # Check what time the scan started
    t1 = datetime.now()
    count=0
    for port in ports:
      connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      port=int(port)
      result = connection.connect_ex((hostname, port))
      if result == 0:
        count=count+1
        print "Port {}:    Open".format(port)
      connection.close()
    
    # Check what time the scan finished
    t2 = datetime.now()
    total =  t2 - t1
    # Printing the information to screen
    print 'Scanning Completed in: ', total
    return count

  except socket.error:
    print "Couldn't connect to server"
    sys.exit()


def main():
  parser = argparse.ArgumentParser(description="Port scanner")
  parser.add_argument("hostname",type=hostname,help="Hostname or  ip address.")
  parser.add_argument("ports",type=ports, help="Single port or list of ports (separated by comma) or range(separated by :")
  args = parser.parse_args()
  count=scan(args.hostname,args.ports)
  print bcolors.OKGREEN + "Found %d open ports" % (count) + bcolors.ENDC


if __name__ == "__main__":
  main()
 