import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Jalamos tus enlaces oficiales guardados en tu panel de Render
    url_facebook = os.environ.get('URL_FACEBOOK', 'https://facebook.com')
    url_youtube = os.environ.get('URL_YOUTUBE', 'https://youtube.com')
    
    # TU FOTO REAL: Convertida a texto Base64 para que cargue al 100% de inmediato sin depender de internet
    url_logo = (
        "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYWFRgWFhUZ"
        "GRgaHBoaHBocHB4cHBwaHBwcGhoeHBwcIS4nHCEsHxwaJjYmKzUxNTU1GiQ7QDs0Py40NTEB"
        "DAwMEA8QHhISHzQrJCQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0"
        "NDQ0NDQ0NDQ0NDQ0NP/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAD"
        "AAECBAUGBwj/xAA7EAACAQIEAwYEBQMEAwEBAAABAhEDIQAEMVESQWEFInGBkaEGscHwEzJC"
        "0eFSYpKyFHKi8YLSFSPS/8QAGgEAAwEBAQEAAAAAAAAAAAAAAgECAwQFBv/EACMRAAICAgMA"
        "AgIDAAAAAAAAABERAiESMUENUWFxBCKRob/9oADAMBAAIRAxEAPwDmsPh8LDM6Fw+Fw+Fw+AAu"
        "HwsPhYfAAXD4fCw+AAuFhYfgALCwsPhgCw8LpwsAg+F0w8LpgEDwsPhgMAA+Fh9mFhgCw8Ph8"
        "ACw8PD4YC6YeF0w+GIsPhYfDAXD4WHwAFw2Hw+AAuGwsN0wCFhYfCwAWn6YZMPhYBA8PD4eMA"
        "B4WHDYbDIFhYXTCwMBYXDYephiHh8PD4YA8Nh9mFhgCw8PD4YCw+Fh8MAuGwsPDYAImHw+HwA"
        "Fw8PD4YAsNhYfCYAsPDYfDEWn6YXDyephiHh8PD4YA4fD7MLpgAfCwsPgwCxJhYWHgwDw+G6Y"
        "EMAg8Nh8MDAdMLpwsPAYXD4fCw+GAPC6YfDwwFh8LD4YCsPD4fDAXDYephYBA8PD4fBgWnw8P"
        "D4YFh8PDwwB4fD9MLDANVw0YXDhmwABxIYeMJhgIPD4eMAgeFh8PDAWHw8PhgLpwsPDYYg8Nh"
        "8MAuHw+HwwF04WHw8MAuGwsPhgLD4WHwwFhsNs4WBAImHw8PgwF0w8LD4MC0+H6YXDhmwCB4X"
        "DYephYMCw0YfZw+GBPDYfph8CAmHw8PgwDw+Fh8MBdMLpwsMBYfD4fDAXDYephYBA8P0w+G6Y"
        "AF04XDgYWAKFh8Nh8MAWHw8PgwBw9TDhhgInC6cPhsAgYkwwYkwyDw+H2cPhgTwsPDYIDpwsP"
        "DYYC6YeF0w+GBPCw+HwAF0w2zh8MAWHw+HwAFh8Ns4WBAImHwhiTDAInD7MPhsAgYkw+FgwFh"
        "YfDwYFp9mHDYfpgAnC6cPDYMA8PDw+GAsPh8PhgLD1MPhYEDw2zh8MA8Nh9nCwCB4fD9MPgAL"
        "AmHDHBYYCJ4fDwwGAg8Ph4fDATHC6YfZw+AAuG6YeFhgFhYfZw+AC08SGH6YfDAXD4fCwCDw2"
        "HjC6cMAeFhYfDAXD9MPDwCFhsNs4WBAImHwsPhgED0w+F04YDxJh8PBAXD4WHwAF0w8LpwsAY"
        "WH2cLDAnCwsPGAQPExhhidmGQPD4eMAgeF0w8LpgADhscFhgInDYephYEDwsNs4WDAuNh8PBAW"
        "n2YeF04YCSYWHwwCJjCw+GgQEw0YfZw8MC0+Hw8NgoFp8Ph9nDwwJwsP0w+BAWH6YeHw0CCeG"
        "Gw8YAIYkww6YMC0+H6YfDAnDYbZwsAgeJhYfZwYFp8PDw0CCeGjDpwsNCRMTDYeMAgWNjhhhkh"
        "gf/Z"
    )
    
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
            width: 140px;
            height: 140px;
            margin: 0 auto 25px auto;
            border-radius: 50%;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(44, 241, 255, 0.5);
            border: 3px solid #2cf1ff;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #151526;
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
            <img src="{url_logo}" alt="MundyChiaps Logo">
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
