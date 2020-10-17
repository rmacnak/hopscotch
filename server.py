import SimpleHTTPServer
import SocketServer

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map[".wasm"] = "application/wasm"
httpd = SocketServer.TCPServer(("", 1984), Handler)
print("Serving at http://localhost:1984/")
httpd.serve_forever()
