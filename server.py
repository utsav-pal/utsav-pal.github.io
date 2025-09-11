#!/usr/bin/env python3
"""
Simple HTTP server for serving static files in Replit environment.
Serves on 0.0.0.0:5000 to work with Replit's proxy system.
"""

import http.server
import socketserver
import os

# Configuration for Replit environment
HOST = "0.0.0.0"  # Must use 0.0.0.0 for Replit
PORT = int(os.getenv("PORT", 5000))  # Use environment PORT for deployment, fallback to 5000 for dev

# Change to the directory containing the static files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add cache control headers to prevent caching issues in Replit iframe
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer((HOST, PORT), handler) as httpd:
        print(f"Server running at http://{HOST}:{PORT}")
        print("Serving static files from current directory")
        httpd.serve_forever()

if __name__ == "__main__":
    main()