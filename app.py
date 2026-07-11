import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # El tubo directo de audio puro
    stream_url = "https://zeno.fm"
    
    # Tus redes sociales enlazadas desde Render
    url_facebook = os.environ.get('URL_FACEBOOK', 'https://facebook.com')
    url_youtube = os.environ.get('URL_YOUTUBE', 'https://youtube.com')

    return f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MundyChiaps Radio Independiente</title>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, #0d0d16, #05050a);
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
                background: rgba(20, 20, 35, 0.7);
                padding: 40px 30px;
                border-radius: 30px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.7);
                border: 1px solid rgba(0, 153, 255, 0.1);
                backdrop-filter: blur(15px);
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .logo-container {{
                width: 140px;
                height: 140px;
                margin-bottom: 20px;
                border-radius: 25px;
                overflow: hidden;
                box-shadow: 0 4px 25px rgba(0, 255, 204, 0.3);
                border: 2px solid #00ffcc;
                background: #000000;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .logo-container svg {{
                width: 80%;
                height: 80%;
            }}
            h1 {{
                font-size: 2.2rem;
                margin: 0 0 5px 0;
                letter-spacing: 2px;
                background: linear-gradient(to right, #00ffcc, #0099ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 800;
            }}
            .status {{
                color: #00ffcc;
                font-size: 0.85rem;
                margin-bottom: 30px;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 3px;
            }}
            
            .play-card {{
                width: 100%;
                background: rgba(255, 255, 255, 0.03);
                padding: 25px;
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                box-sizing: border-box;
                margin-bottom: 30px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .custom-play-btn {{
                width: 80px;
                height: 80px;
                background: linear-gradient(135deg, #00ffcc, #0099ff);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                box-shadow: 0 6px 20px rgba(0, 255, 204, 0.4);
                transition: transform 0.2s, box-shadow 0.2s;
                border: none;
                outline: none;
            }}
            .custom-play-btn:hover {{
                transform: scale(1.08);
                box-shadow: 0 8px 25px rgba(0, 255, 204, 0.6);
            }}
            .play-icon {{
                width: 0;
                height: 0;
                border-top: 15px solid transparent;
                border-bottom: 15px solid transparent;
                border-left: 25px solid #ffffff;
                margin-left: 6px;
            }}
            .pause-icon {{
                display: none;
                width: 20px;
                height: 25px;
                border-left: 6px solid #ffffff;
                border-right: 6px solid #ffffff;
            }}
            .player-text {{
                margin-top: 15px;
                font-size: 0.9rem;
                color: #a0a0b8;
                font-weight: 500;
            }}

            .social-bar {{
                width: 100%;
                display: flex;
                flex-direction: column;
                gap: 12px;
            }}
            .btn {{
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                padding: 15px;
                border-radius: 14px;
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
            <div class="status">● SEÑAL EN VIVO</div>
            
            <div class="play-card">
                <button class="custom-play-btn" id="masterPlayBtn" onclick="toggleRadioStream()">
                    <div class="play-icon" id="playIcon"></div>
                    <div class="pause-icon" id="pauseIcon"></div>
                </button>
                <div class="player-text" id="statusText">Haga clic para escuchar la radio</div>
            </div>

            <div class="social-bar">
                <a href="{url_facebook}" target="_blank" class="btn btn-facebook">Página de Facebook</a>
                <a href="{url_youtube}" target="_blank" class="btn btn-youtube">Canal de YouTube</a>
            </div>
        </div>

        <script>
            var radioAudio = null;
            var isStreaming = false;
            var streamEndpoint = "{stream_url}";

            function toggleRadioStream() {{
                var pIcon = document.getElementById("playIcon");
                var pauseIcon = document.getElementById("pauseIcon");
                var sText = document.getElementById("statusText");

                if (!isStreaming) {{
                    sText.innerText = "Conectando al tubo de audio...";
                    
                    radioAudio = new Audio();
                    radioAudio.crossOrigin = "anonymous";
                    radioAudio.src = streamEndpoint + "?cachebuster=" + Date.now();
                    radioAudio.preload = "none";

                    radioAudio.play().then(function() {{
                        isStreaming = true;
                        pIcon.style.display = "none";
                        pauseIcon.style.display = "block";
                        sText.innerText = "Sintonizando señal digital en vivo";
                    }}).catch(function(error) {{
                        console.log("Error de proteccion:", error);
                        sText.innerText = "Reintentando conexion segura...";
                        radioAudio.src = streamEndpoint;
                        radioAudio.play();
                    }});
                }} else {{
                    if (radioAudio) {{
                        radioAudio.pause();
                        radioAudio.src = "";
                        radioAudio = null;
                    }}
                    isStreaming = false;
                    pIcon.style.display = "block";
                    pauseIcon.style.display = "none";
                    sText.innerText = "Radio en pausa";
                }}
            }}
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
