from http.server import SimpleHTTPRequestHandler, HTTPServer
import webbrowser
import os

PORT = 8000
WEB_DIR = os.path.dirname(os.path.abspath(__file__))

class RequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'服务器启动在 http://localhost:{PORT}')
    webbrowser.open(f'http://localhost:{PORT}/index.html')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()