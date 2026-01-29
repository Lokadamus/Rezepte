#!/usr/bin/env python3
"""
Einfacher Server für Pichlhofers Rezeptsammlung
Startet mit: python3 server.py
Öffne dann: http://localhost:8000
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os

PORT = 8000
REZEPTE_FILE = 'rezepte.json'

class RezepteHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        # Rezepte speichern
        if self.path == '/api/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                rezepte = json.loads(post_data.decode('utf-8'))

                # In Datei speichern
                with open(REZEPTE_FILE, 'w', encoding='utf-8') as f:
                    json.dump(rezepte, f, ensure_ascii=False, indent=2)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True}).encode())
                print(f"✓ {len(rezepte)} Rezepte gespeichert")

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
                print(f"✗ Fehler: {e}")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    server = HTTPServer(('0.0.0.0', PORT), RezepteHandler)
    print(f"""
╔════════════════════════════════════════════╗
║   Pichlhofers Rezeptsammlung - Server      ║
╠════════════════════════════════════════════╣
║   Öffne im Browser:                        ║
║   → http://localhost:{PORT}                   ║
║                                            ║
║   Beenden mit: Ctrl+C                      ║
╚════════════════════════════════════════════╝
""")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer beendet.")
