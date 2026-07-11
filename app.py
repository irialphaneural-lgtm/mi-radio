from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Flujo de audio limpio y directo de tu señal de Zeno (sin páginas web)
    stream_url = "https://zeno.fm"
    
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
                background: #1e1e2f;
                padding: 35px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.5);
                border: 1px solid rgba(255,255,255,0.1);
                text-align: center;
                width: 85%;
                max-width: 400px;
            }}
            h1 {{
                font-size: 1.8rem;
                margin-top: 0;
                margin-bottom: 5px;
                background: linear-gradient(to right, #00ffcc, #0099ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            p {{
                color: #a0a0b8;
                margin-bottom: 25px;
                font-size: 0.9rem;
            }}
            audio {{
                width: 100%;
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
        <!-- Caja del Reproductor Nativo sin bloqueos de Zeno -->
        <div class="player-container">
            <h1>MUNDYCHIAPS</h1>
            <p>Señal Digital en Vivo</p>
            <audio controls autoplay preload="none">
                <source src="{stream_url}" type="audio/mpeg">
                Tu navegador no soporta este reproductor de audio.
            </audio>
        </div>

        <!-- Botones flotantes directos a tus páginas -->
        <div class="social-bar">
            <a href="{url_facebook}" target="_blank" class="btn btn-facebook">Facebook</a>
            <a href="{url_youtube}" target="_blank" class="btn btn-youtube">YouTube</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
