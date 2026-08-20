from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Tell the frontend browser that everything went perfectly (Status 200)
        self.send_response(200)
        
        # 2. Tell the browser we are sending back a cleanly structured JSON package
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # 3. Create the data payload message
        data = {
            "message": "Success! Your Python backend script processed this request live!"
        }
        
        # 4. Ship the package out across the internet pipeline
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
