import json
import os
import platform
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = os.getenv("WORLDOS_HOST", "0.0.0.0")
PORT = int(os.getenv("WORLDOS_PORT", "8080"))


class WorldOSHandler(BaseHTTPRequestHandler):
    server_version = "WorldOS-Server/0.1.0"

    def _send_json(self, status, data):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/" or self.path == "/api/status":
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
                "python": platform.python_version()
            })
            return

        self._send_json(404, {
            "error": "Not found"
        })

    def log_message(self, format, *args):
        print(f"[WorldOS] {self.address_string()} - {format % args}")


def main():
    server = ThreadingHTTPServer((HOST, PORT), WorldOSHandler)
    print(f"WorldOS Server läuft auf http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("WorldOS Server wird beendet.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
