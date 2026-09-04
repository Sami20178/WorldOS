#!/usr/bin/env python3
"""WorldOS HTTP server."""

import json
import os
import platform
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = os.environ.get("WORLDOS_HOST", "0.0.0.0")
PORT = int(os.environ.get("WORLDOS_PORT", "8080"))


class WorldOSHandler(BaseHTTPRequestHandler):
    server_version = "WorldOS/0.1.0"

    def _send_json(self, status, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send_json(204, {})

    def do_GET(self):
        if self.path in ("/", "/api/status"):
            self._send_json(200, {
                "name": "WorldOS",
                "server": "online",
                "version": "0.1.0"
            })
            return

        if self.path == "/api/system":
            self._send_json(200, {
                "platform": platform.system(),
                "release": platform.release(),
                "architecture": platform.machine(),
                "python": sys.version.split()[0]
            })
            return

        self._send_json(404, {
            "error": "Not Found",
            "path": self.path
        })

    def log_message(self, format_string, *args):
        print("[WorldOS] " + format_string % args)


def main():
    httpd = ThreadingHTTPServer((HOST, PORT), WorldOSHandler)
    print(f"WorldOS server running on http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nWorldOS server stopping")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
