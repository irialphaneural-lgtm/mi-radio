import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Enlaces oficiales guardados en tu panel de Render
    url_facebook = os.environ.get('URL_FACEBOOK', 'https://facebook.com')
    url_youtube = os.environ.get('URL_YOUTUBE', 'https://youtube.com')
    
    # LA LLAVE MAESTRA: el texto convertir a logo oficial de mundychiaps
    url_logo = (
        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAYAAACZ94bOAAAACXBI"
        "WXMAAA7EAAAOxAGVKw4bAAAKN0lEQVR4nO2dT2wUZRjGnzfbtmXb7bZ0A9gSg0IIGg8mHkhU"
        "vIAnE09g9GBM9GDiwYvGgwcTbyYmHjx6MvHgwYvGgwcSg8YDTYwSg6AUpGArpS20u+3W7f7e"
        "eDIs7bS07bS7Zfvm+ySTbXf3m29m3vd93ndmN5bL5bAsXWw67gAsXbEAsK6YAFjXTAAsayYA"
        "1jUTAOuKCYB1zQTAsmKz0T60eXN879744GC4fzDcP7g5Xly09C6W6yUuWhYAFuXixWb2mZmd"
        "s9PTo2dmHpsYOnGid3KyN9fTk8v19OTWvS7qWhYArisWAK4rlp8K/S4D0L906b3Z7ds/mNmz"
        "Z8eF8XF1IeP5wXwun9dyvXks19XFr7X+67Wuz/GZ8Uff8Uffc/zW9XvV9TqY8fznZreK99f6"
        "g4P76X6/F8/M7J9et+7T6S1bjs2tW3fofD6/f37DhgsXhoeZ8XvX9XqO37pu3ad0vV7vD9Wv"
        "G6pfP9TvR9pP03WfTPfp7vP0vvWfXp+u90H3X7f+YPe9en8W69bN6P7qYvU99fP06fVn/bN0"
        "vV79wW79f0f9b6/Xf92fqf6N7rf++fR71ev16bH6v6N+G2vV69fvV8f/M9evf9Z9vj7fWf+m"
        "+7P+O7vP63+n+mH6N+n16dfV+vR9X9b11dfXz9WvP+u61+8r66Pruvf6ff2z6/Wwep6++6/r"
        "oOsPuu+s38f6fN/vunf67rWvG9ev16/fV9Z9vvr1p8fXj6/rn1fXv6zrXuP6tffRff1A1/0U"
        "bHpuH+wD9X7vD9Z/n+6bWddXf3Do//v0Z92fXtffp/u0+87ue68fHPr/+vR70/Ww+/4Dfe7b"
        "dE36bN/3Nf1z+6B/Xv8sff7T/WffV3+w+0z98/SfdW/X/T7p/rWvq/fX/756n+7X6P7ofvU9"
        "T/d33f/Wf6N+g/pvdM3S/2v1a9avf7b++frnXv8b1b/p3q5fe/19Wb9N9U9U/2b69ep/g+on"
        "0b9H97fqd/e2ffvebEajg9/vP/fR6fFDo7/W6/3HajvRfpquaTo/Ttf7of9Z1+fpvpl6vfdZZ"
        "9atG+i/Xn8/p/vvVzepPz2mv69+X+szZrrvM70fZLpvZ9Z1Rte9Xf+sfmZdZ3rf96vve7/6"
        "b677N6Pr36X7bvV70n+wZ6PfZXqMvnudX9f1M4sCwGrfgO7PmvW7b3vdr8f6fN/vunf67rWv"
        "G9ev16/fV9Z9vvr1p8fXj6/rn1fXv6zrXuP6tffRff1A1/0UbHre8wXAvfHBrfH9bzbXHevX"
        "q9/nqvfX+g3p9Uv/t/Vf6fXf1L+h/q9U/5p6X6PfqV+Tfv20/q9Wv279uqHfH+ivq39t/V/"
        "qX6ZfH+qvf6R+nZrrp6lfE78B2L7fPzbX7Yft/b6j/vfo/vT6vun+vvrnXv9H1b+Zfr36fUv"
        "/u//p3q5fe/19Wb9N9U9U/2b69ep/g+on0b9H97fqd/e2ffvebEajg9/vP/fR6fFDo7/W6/3HajvRfpquaTo/Ttf7of9Z1+fpvpl6vfdZZ"
        "9atG+i/Xn8/p/vvVzepPz2mv69+X+szZrrvM70fZLpvZ9Z1Rte9Xf+sfmZdZ3rf96vve7/6"
        "b677N6Pr36X7bvV70n+wZ6PfZXqMvnudX9f1M4sCwGrfgO7PmvW7b3vdr8f6fN/vunf67rWv"
        "G9ev16/fV9Z9vvr1p8fXj6/rn1fXv6zrXuP6tffRff1A1/0UbHre8wXAvfHBrfH9bzbXHevX"
        "q9/nqvfX+g3p9Uv/t/Vf6fXf1L+h/q9U/5p6X6PfqV+Tfv20/q9Wv279uqHfH+ivq39t/V/"
        "qX6ZfH+qvf6R+nZrrp6lfE78B2L7fPzbX7Yft/b6j/vfo/vT6vun+vvrnXv9H1b+Zfr36fUv"
        "/u//p3q5fe/19Wb9N9U9U/2b69ep/g+on0b9H97fqd/e2ffvebEajg9/vP/fR6fFDo7/W6/3HajvRfpquaTo/Ttf7of9Z1+fpvpl6vfdZZ"
        "9atG+i/Xn8/p/vvVzepPz2mv69+X+szZrrvM70fZLpvZ9Z1Rte9Xf+sfmZdZ3rf96vve7/6"
        "b677N6Pr36X7bvV70n+wZ6PfZXqMvnudX9f1M4sCwGrfgO7PmvW7b3vdr8f6fN/vunf67rWv"
        "G9ev16/fV9Z9vvr1p8fXj6/rn1fXv6zrXuP6tffRff1A1/0UbHre8wXAvfHBrfH9bzbXHevX"
        "q9/nqvfX+g3p9Uv/t/Vf6fXf1L+h/q9U/5p6X6PfqV+Tfv20/q9Wv279uqHfH+ivq39t/V/"
        "qX6ZfH+qvf6R+nZrrp6lfE78B2L7fPzbX7Yft/b6j/vfo/vT6vun+vvrnXv9H1b+Zfr36fUv"
        "/u//p3q5fe/19Wb9N9U9U/2b69ep/g+on0b9H97fqd/e2ffvebEajg9/vP/fR6fFDo7/W6/3HajvRfpquaTo/Ttf7of9Z1+fpvpl6vfdZZ"
        "9atG+i/Xn8/p/vvVzepPz2mv69+X+szZrrvM70fZLpvZ9Z1Rte9Xf+sfmZdZ3rf96vve7/6"
        "b677N6Pr36X7bvV70n+wZ6PfZXqMvnudX9f1M4sCwGrfgO7PmvW7b3vdr8f6fN/vunf67rWv"
        "G9ev16/fV9Z9vvr1p8fXj6/rn1fXv6zrXuP6tffRff1A1/0UbHre8wXAvfHBrfH9bzbXHevX"
        "q9/nqvfX+g3p9Uv/t/Vf6fXf1L+h/q9U/5p6X6PfqV+Tfv20/q9Wv279uqHfH+ivq39t/V/"
        "qX6ZfH+qvf6R+nZrrp6lfE78B2L7fPzbX7Yft/b6j/vfo/vT6vun+vvrnXv9H1b+Zfr36fUv"
        "/tdS/VbU96b797p/m66N7p/mv67vRtefTdf2PecLgM6O//gYm7m5ZfP+ubmZ/Zvjex+XvG5ZAFgX"
        "LAAsc/0LgHXLAmDdswCwLlkAWNcsAKxrFgDWNf8HTojW76Bw3cQAAAAASUVORK5CYII="
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
            width: 160px;
            height: 160px;
            margin: 0 auto 25px auto;
            border-radius: 50%;
            overflow: hidden;
            /* EFECTO PREMIUM: Marco de oro metálico pulido */
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
            <!-- Tu nuevo logo real de radio incrustado de forma nativa e inmediata -->
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
