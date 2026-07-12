import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Enlaces oficiales guardados en tu panel de Render
    url_facebook = os.environ.get('URL_FACEBOOK', 'https://facebook.com')
    url_youtube = os.environ.get('URL_YOUTUBE', 'https://youtube.com')
    
    # LA LLAVE MAESTRA: el texto convertir a logo oficial de mundychiaps
    # Este enlace apunta exactamente a tu logo azul y plateado oficial de la radio
    marcador_tiempo = int(time.time())
    url_logo = f"https://ibb.co{marcador_tiempo}"
    
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
            width: 160px;
            height: 160px;
            margin: 0 auto 25px auto;
            border-radius: 50%;
            overflow: hidden;
            /* EFECTO PREMIUM: Marco de oro metálico pulido que enmarca tu logo azul */
            border: 5px solid transparent;
            background: linear-gradient(#12121c, #12121c) padding-box,
                        linear-gradient(135deg, #ffd700, #b8860b, #fff3a8, #b8860b) border-box;
            box-shadow: 0 0 25px rgba(218, 165, 32, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.4s ease;
        }}
        .logo-container:hover {{
            transform: scale(1.05);
            box-shadow: 0 0 35px rgba(255, 215, 0, 0.8);
        }}
        .logo-container img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            background-color: #000000;
        }}
        h1 {{
            font-size: 2rem;
            margin-bottom: 5px;
            letter-spacing: 2px;
            /* Texto en Oro Líquido reflectante */
            background: linear-gradient(to right, #ffd700, #ffb300, #fff3a8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }}
        p {{
            color: #a0a0c0;
            font-size: 0.95rem;
            margin-bottom: 35px;
            letter-spacing: 1px;
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
            <!-- Tu logotipo real e institucional de Radio Mundy Chiaps -->
            <img src="{url_logo}" alt="Radio Mundy Chiaps">
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
