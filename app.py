import os
import http.server
import socketserver

# Sesuai PPT Pak Irfan
if not os.path.exists('cloud-tugas'):
    os.makedirs('cloud-tugas')
os.chdir('cloud-tugas')

# Pakai nama variabel dari PPT (tapi typo DOCTYPE aku benerin ya)
jls_extract_var = """<!DOCTYPE html>
<html>
<head>
    <title>Tugas Cloud Computing - TI UIN Salatiga</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding: 50px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
        }
        .container {
            background: rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            margin: auto;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        h1 { font-size: 3em; margin-bottom: 0; }
        .subtitle { font-size: 1.5em; color: #ffd700; }
        .info { margin-top: 30px; font-size: 0.9em; opacity: 0.9; }
    </style>
</head>
<body>
    <div class="container">
        <h1>&#9729; Cloud Computing</h1>
        <div class="subtitle">TI UIN Salatiga</div>
        <p>&#9731; Tugas praktikum berhasil dijalankan di <strong>Google Cloud Shell</strong></p>
        <p>&#9732; Web server berjalan di lingkungan cloud tanpa kartu kredit!</p>
        <hr>
        <div class="info">
            Nama: Keyren Laura Avanti <br>
            NIM : 43050250086
        </div>
    </div>
</body>
</html>
"""

html_content = jls_extract_var

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Server berjalan di port {PORT}")
    print(f"🔍 CARA PREVIEW:")
    print(f"1. Klik ikon 'Web Preview' di pojok kanan atas.")
    print(f"2. Pilih 'Preview on port {PORT}'.")
    httpd.serve_forever()