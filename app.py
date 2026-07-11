import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Enlaces oficiales guardados en tu panel de Render
    url_facebook = os.environ.get('URL_FACEBOOK', 'https://facebook.com')
    url_youtube = os.environ.get('URL_YOUTUBE', 'https://youtube.com')

    return f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MundyChiaps Oficial</title>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, #12121c, #08080f);
                color: #ffffff;
                font-family: 'Segoe UI', Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                width: 90%;
                max-width: 400px;
                text-align: center;
                background: rgba(30, 30, 47, 0.6);
                padding: 40px 30px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.5);
                border: 1px solid rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .logo-container {{
                width: 140px;
                height: 140px;
                margin-bottom: 25px;
                border-radius: 20px;
                overflow: hidden;
                box-shadow: 0 4px 20px rgba(0, 153, 255, 0.4);
                border: 2px solid #0099ff;
                background: #000000;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .logo-container svg {{
                width: 85%;
                height: 85%;
            }}
            h1 {{
                font-size: 2rem;
                margin: 0 0 5px 0;
                letter-spacing: 1px;
                background: linear-gradient(to right, #00ffcc, #0099ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            p {{
                color: #8a8ab0;
                font-size: 0.95rem;
                margin: 0 0 35px 0;
            }}
            .btn {{
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                padding: 15px;
                margin: 10px 0;
                border-radius: 12px;
                text-decoration: none;
                font-weight: bold;
                font-size: 1.1rem;
                color: #ffffff;
                transition: transform 0.2s, box-shadow 0.2s;
                box-sizing: border-box;
            }}
            .btn:hover {{
                transform: translateY(-3px);
            }}
            .btn-facebook {{
                background-color: #1877F2;
                box-shadow: 0 4px 15px rgba(24, 119, 242, 0.3);
            }}
            .btn-youtube {{
                background-color: #FF0000;
                box-shadow: 0 4px 15px rgba(255, 0, 0, 0.3);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Logotipo vectorial integrado directamente en código libre de errores -->
            <div class="logo-container">
                <svg viewBox="0 0 100 100" xmlns="http://w3.org">
                    <rect x="10" y="25" width="80" height="60" rx="10" fill="none" stroke="#0099ff" stroke-width="4"/>
                    <line x1="10" y1="65" x2="90" y2="65" stroke="#0099ff" stroke-width="2"/>
                    <circle cx="30" cy="75" r="4" fill="#ffd700"/>
                    <circle cx="45" cy="75" r="4" fill="#ffd700"/>
                    <line x1="60" y1="72" x2="80" y2="72" stroke="#ffd700" stroke-width="3"/>
                    <line x1="60" y1="78" x2="80" y2="78" stroke="#ffd700" stroke-width="3"/>
                    <circle cx="50" cy="45" r="14" fill="none" stroke="#00ffcc" stroke-width="3"/>
                    <path d="M40,45 A10,10 0 0,1 60,45" fill="none" stroke="#ffd700" stroke-width="2"/>
                    <path d="M42,48 Q50,55 58,48" fill="none" stroke="#00ffcc" stroke-width="2"/>
                    <line x1="30" y1="10" x2="45" y2="25" stroke="#ffd700" stroke-width="3"/>
                    <line x1="70" y1="10" x2="55" y2="25" stroke="#ffd700" stroke-width="3"/>
                    <circle cx="30" cy="10" r="3" fill="#ff00ff"/>
                    <circle cx="70" cy="10" r="3" fill="#ff00ff"/>
                </svg>
            </div>
            <h1>MUNDYCHIAPS</h1>
            <p>Nuestras Redes Oficiales</p>
            
            <a href="{url_facebook}" target="_blank" class="btn btn-facebook">Página de Facebook</a>
            <a href="{url_youtube}" target="_blank" class="btn btn-youtube">Canal de YouTube</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
