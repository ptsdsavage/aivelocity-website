"""
Simple local dev server that serves .html files without requiring the extension in the URL.
Usage: python3 server.py
"""
import http.server
import os

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Strip query string for file lookup
        path = self.path.split('?')[0].split('#')[0]

        # If path has no extension and isn't a directory, try appending .html
        if '.' not in os.path.basename(path):
            html_path = path.rstrip('/') + '.html'
            local_path = os.path.join(os.getcwd(), html_path.lstrip('/'))
            if os.path.isfile(local_path):
                self.path = html_path

        return super().do_GET()

if __name__ == '__main__':
    PORT = 8000
    with http.server.HTTPServer(('', PORT), CleanURLHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
