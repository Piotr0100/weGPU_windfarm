"""Tiny static server for the WebGPU demo.

Usage:
    python serve.py            # serves on http://localhost:8000
    python serve.py 9000       # custom port

WebGPU requires a secure context — localhost counts, file:// does not.
"""

import http.server
import socketserver
import sys
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "application/javascript",
        ".mjs": "application/javascript",
        ".wasm": "application/wasm",
        ".glb": "model/gltf-binary",
        ".gltf": "model/gltf+json",
        ".hdr": "application/octet-stream",
        ".exr": "application/octet-stream",
        ".map": "application/json",
    }

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


os.chdir(DIR)

with socketserver.ThreadingTCPServer(("127.0.0.1", PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving {DIR}")
    print(f"  -> http://localhost:{PORT}/")
    print("Ctrl+C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
