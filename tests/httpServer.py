#!/usr/bin/env python3

import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        SimpleHTTPRequestHandler.end_headers(self)

    # Don't log successful requests to minimize test automation output.
    def log_request(self, code='-', size='-'): pass

port = 8000
if len(sys.argv) > 1:
    port = int(sys.argv[1])

httpd = HTTPServer(('', port), CustomRequestHandler)
httpd.serve_forever()
