from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class MyHTTPHandler(BaseHTTPRequestHandler):
    time_requests = 0

    def do_GET(self):
        if self.path == '/time':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.wfile.write(current_time.encode())

            MyHTTPHandler.time_requests += 1
            with open('statistics.txt', 'w') as file:
                file.write(str(MyHTTPHandler.time_requests))

        elif self.path == '/statistics':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(MyHTTPHandler.time_requests).encode())

        else:
            self.send_error(404, 'Not Found')

def run(server_class=HTTPServer, handler_class=MyHTTPHandler, port=8888):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server stopped.')

if __name__ == '__main__':
    run()

