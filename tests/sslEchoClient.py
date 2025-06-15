#!/usr/bin/env python3

import socket
import ssl
import pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s,
                          ca_certs="cert.pem",
                          cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('localhost', 54443))

text = 'Hello, world!'

ssl_sock.write(text.encode())
print("send: " + text)
data = ssl_sock.read().decode()
print("recv: " + data)

ssl_sock.close()
