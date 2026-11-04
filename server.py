#!/usr/bin/env python3
import http.server, json, urllib.parse, os
PORT = int(os.environ.get("PORT", 8080))

class IPRiskHandler(http.server.BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        if self.path in ("/health", "/v1/health", "/"):
            self.send_json({"status": "healthy", "service": "IPRisk API", "version": "1.0.0", "uptime": "99.99%"})
            return
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)
        ip = qs.get("ip", ["1.1.1.1"])[0]
        self.send_json({
            "success": True,
            "ip": ip,
            "risk_score": 0.05,
            "is_vpn": False,
            "is_tor": False,
            "is_datacenter": True if ip.startswith("1.") else False,
            "is_crawler": False,
            "fraud_recommendation": "ALLOW"
        })

if __name__ == "__main__":
    http.server.HTTPServer(("0.0.0.0", PORT), IPRiskHandler).serve_forever()
