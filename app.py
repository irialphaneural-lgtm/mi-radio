import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Lee el enlace de tu transmisión guardado en Render
    url = os.environ.get('URL_ZENO', '')
    
    # Crea el diseño de pantalla completa sin márgenes ni textos
    return f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MundyChiaps Radio</title>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                background-color: #000000;
            }}
            iframe {{
                width: 100%;
                height: 100%;
                border: none;
                display: block;
            }}
        </style>
    </head>
    <body>
        <iframe src="{url}"></iframe>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
