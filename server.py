#!/usr/bin/env python3

import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map[".wasm"] = "application/wasm"
httpd = socketserver.TCPServer(("", 1984), Handler)
print("Serving at http://localhost:1984/")
httpd.serve_forever()
