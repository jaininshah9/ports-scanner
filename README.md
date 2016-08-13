# ports-scanner
Scan for open ports on a server

# Usage
```
$ python port_scanner.py --help
usage: port_scanner.py [-h] hostname ports

Port scanner

positional arguments:
  hostname    Hostname or ip address.
  ports       Single port or list of ports (separated by comma) or
              range(separated by :

optional arguments:
  -h, --help  show this help message and exit
```

# Examples

```
$ python port_scanner.py localhost 22
------------------------------------------------------------
Please wait, scanning host localhost
------------------------------------------------------------
Port 22:    Open
Scanning Completed in:  0:00:00.000244
Found 1 open ports
```

```
$ python port_scanner.py localhost 22:112
------------------------------------------------------------
Please wait, scanning host localhost
------------------------------------------------------------
Port 22:    Open
Port 111:    Open
Scanning Completed in:  0:00:00.005207
Found 2 open ports
```

```
$ python port_scanner.py localhost 22,111
------------------------------------------------------------
Please wait, scanning host localhost
------------------------------------------------------------
Port 22:    Open
Port 111:    Open
Scanning Completed in:  0:00:00.000348
Found 2 open ports
```
