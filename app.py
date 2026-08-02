import streamlit as st
import os

# 1. Configuración de la página del navegador
st.set_page_config(
    page_title="MundyChiaps Oficial",
    page_icon="cabina.jpg",
    layout="centered"
)

# 2. Estilos personalizados para el contenedor y los botones estilo Linktree
st.markdown("""
    <style>
        /* Ocultar elementos por defecto de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Fondo degradado oscuro */
        .stApp {
            background: linear-gradient(135deg, #12121c, #08080f) !important;
        }
        
        /* Contenedor principal centrado */
        .main-container {
            text-align: center;
            max-width: 400px;
            margin: 0 auto;
            padding: 30px;
            background: rgba(30, 30, 47, 0.6);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
        }
        
        /* Letras doradas del título */
        .main-title {
            font-size: 2rem !important;
            font-weight: 800 !important;
            letter-spacing: 2px;
            margin-top: 15px !important;
            margin-bottom: 5px !important;
            background: linear-gradient(to right, #ffd700, #fff3a8, #ffd700);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        
        .sub-title {
            color: #a0a0c0;
            font-size: 0.95rem;
            margin-bottom: 30px;
            text-align: center;
            letter-spacing: 1px;
        }
        
        /* Botones personalizados */
        .custom-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 15px;
            margin: 15px 0;
            border-radius: 12px;
            text-decoration: none !important;
            font-weight: bold;
            font-size: 1.1rem;
            color: #ffffff !important;
            transition: transform 0.2s, box-shadow 0.2s;
            text-align: center;
        }
        .custom-btn:hover {
            transform: translateY(-3px);
        }
        .btn-fb {
            background-color: #1877F2;
            box-shadow: 0 4px 15px rgba(24, 119, 242, 0.3);
        }
        .btn-yt {
            background-color: #FF0000;
            box-shadow: 0 4px 15px rgba(255, 0, 0, 0.3);
        }
    </style>
""", unsafe_allow_index=False, unsafe_allow_html=True)

# Variables de entorno para tus redes
url_facebook = os.environ.get('URL_FACEBOOK', 'https://facebook.com')
url_youtube = os.environ.get('URL_YOUTUBE', 'https://youtube.com')

# 3. Renderizado de la interfaz
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Mostrar el logo circular de forma nativa con Python usando columnas para centrarlo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Python lee directamente el archivo de tu lista usando su nombre exacto
    st.image("cabina.jpg", use_column_width=True, output_format="JPEG")

# Título y Subtítulo
st.markdown('<p class="main-title">MUNDYCHIAPS</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Nuestras Redes Oficiales</p>', unsafe_allow_html=True)

# Botones de las Redes Sociales
st.markdown(f'<a href="{url_facebook}" target="_blank" class="custom-btn btn-fb">Página de Facebook</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{url_youtube}" target="_blank" class="custom-btn btn-yt">Canal de YouTube</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
