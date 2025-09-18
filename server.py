import http.server
import socketserver

PORT = 5000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
   
    print("\033c\033[43;30m\nserving at port", PORT)
    httpd.serve_forever()