import http.server
import socketserver
import socket
import os

from whiplash import __version__


def find_free_port(start_port=3000):
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1


def run():
    port = find_free_port(3000)
    directory = os.getcwd()

    print(f"Whiplash v{__version__}")
    print(f"Serving: {directory}")
    print(f"Localhost port: {port}")
    print("Status: Active\n")

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
        print(f"\nShutting down: {port}")
