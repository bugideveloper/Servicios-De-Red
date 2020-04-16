import http.server
import socketserver

#[Referencias]
#Faltan Metodo Get y Post
#https://blog.anvileight.com/posts/simple-python-http-server/
#https://www.afternerd.com/blog/python-http-server/

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()