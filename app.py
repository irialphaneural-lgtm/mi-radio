import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Jalamos tus enlaces oficiales guardados en tu panel de Render
    url_facebook = os.environ.get('URL_FACEBOOK', '#')
    url_youtube = os.environ.get('URL_YOUTUBE', '#')
    
    # Ruta corregida 100% en minúsculas para evitar bloqueos de GitHub
    url_logo = "https://githubusercontent.com"

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
            }}
            .logo-container {{
                width: 130px;
                height: 130px;
                margin: 0 auto 25px auto;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 4px 20px rgba(0, 153, 255, 0.4);
                border: 2px solid #0099ff;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #000000;
            }}
            .logo-container img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
            }}
            h1 {{
                font-size: 2rem;
                margin-bottom: 5px;
                letter-spacing: 1px;
                background: linear-gradient(to right, #00ffcc, #0099ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            p {{
                color: #8a8ab0;
                font-size: 0.95rem;
                margin-bottom: 35px;
            }}
            .btn {{
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                padding: 15px;
                margin: 15px 0;
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
            <div class="logo-container">
                <img src="{url_logo}" alt="MundyChiaps Logo" onerror="this.src='https://placehold.co'">
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
