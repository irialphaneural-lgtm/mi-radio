from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Widget oficial con parámetros nocturnos para evitar bloqueos
    widget_url = "https://zeno.fm"
    
    # Enlaces oficiales exactos de tus páginas de MundyChiaps
    url_facebook = "https://facebook.com"
    url_youtube = "https://youtube.com"

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
                background-color: #0f0f1a;
                font-family: 'Segoe UI', Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
            .player-container {{
                width: 95%;
                max-width: 450px;
                height: 180px;
                background: #1e1e2f;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 8px 32px rgba(0,0,0,0.5);
                border: 1px solid rgba(255,255,255,0.1);
            }}
            iframe {{
                width: 100%;
                height: 100%;
                border: none;
                display: block;
            }}
            .social-bar {{
                position: fixed;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                gap: 15px;
                z-index: 9999;
                background: rgba(15, 15, 26, 0.9);
                padding: 10px 20px;
                border-radius: 30px;
                backdrop-filter: blur(5px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            .btn {{
                padding: 8px 16px;
                border-radius: 20px;
                text-decoration: none;
                font-weight: bold;
                font-size: 0.9rem;
                color: #ffffff;
                transition: transform 0.2s;
            }}
            .btn:hover {{
                transform: translateY(-3px);
            }}
            .btn-facebook {{ background-color: #1877F2; }}
            .btn-youtube {{ background-color: #FF0000; }}
        </style>
    </head>
    <body>
        <!-- Contenedor forzado con permisos de audio integrados -->
        <div class="player-container">
            <iframe src="{widget_url}" allow="autoplay; encrypted-media"></iframe>
        </div>

        <!-- Botones flotantes directos a tus páginas oficiales -->
        <div class="social-bar">
            <a href="{url_facebook}" target="_blank" class="btn btn-facebook">Facebook</a>
            <a href="{url_youtube}" target="_blank" class="btn btn-youtube">YouTube</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
