#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

# This is a copy of _RESTRICTED_SERVER_CIPHERS from the current tip of ssl.py
# <https://hg.python.org/cpython/file/af793c7580f1/Lib/ssl.py#l174> except that
# RC4 has been added back in, since it was removed in Python 2.7.10,
# but SSLStreamConnection only supports RC4 ciphers.
CIPHERS = (
    'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
    'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:'
    '!eNULL:!MD5:!DSS:RC4'
)

httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'cert.pem')
context.set_ciphers(CIPHERS)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
