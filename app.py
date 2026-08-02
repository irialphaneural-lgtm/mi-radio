import streamlit as st
import os

# 1. Configuración de la pestaña del navegador
st.set_page_config(
    page_title="MundyChiaps Oficial",
    page_icon="cabina.jpg",
    layout="centered"
)

# 2. Estilos visuales personalizados extraídos de tu respaldo
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background: linear-gradient(135deg, #12121c, #08080f) !important;
    }
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
        color: #ffd700;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 20px;
        text-align: center;
        letter-spacing: 1px;
        line-height: 1.4;
    }
    .info-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        text-align: left;
    }
    .info-text {
        color: #e0e0e0;
        font-size: 0.95rem;
        line-height: 1.6;
        margin: 8px 0;
    }
    .info-highlight {
        color: #fff3a8;
        font-weight: bold;
    }
    .founder-link {
        color: #1877F2 !important;
        text-decoration: none !important;
        font-weight: bold;
    }
    .founder-link:hover {
        text-decoration: underline !important;
        color: #4facfe !important;
    }
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
    .btn-app {
        background: linear-gradient(135deg, #10b981, #059669);
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
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
""", unsafe_allow_html=True)

url_facebook = os.environ.get('URL_FACEBOOK', 'https://facebook.com')
url_youtube = os.environ.get('URL_YOUTUBE', 'https://youtube.com')
url_pedro_perfil = "https://facebook.com"
url_descarga_app = "https://www.appcreator24.com/app4114346-4cv160"

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Contenedor superior con tu mensaje de bienvenida
st.markdown("""
    <div style="background: rgba(255, 215, 0, 0.1); border: 1px solid #ffd700; padding: 12px; border-radius: 10px; margin-bottom: 25px; text-align: center;">
        <p style="color: #ffd700; font-weight: bold; margin: 0; font-size: 1.1rem; letter-spacing: 2px;">
            📢 BIENVENIDOS A MUNDYCHIAPS
        </p>
    </div>
""", unsafe_allow_html=True)

# Tu código nativo del respaldo para centrar la cabina
coll1, col2, col3 = st.columns()
with col2:
    st.image("cabina.jpg", width=350)

st.markdown('<p class="main-title">MUNDYCHIAPS</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Emisora virtual en apoyo a compositores emergentes</p>', unsafe_allow_html=True)

# Cuadro oficial de datos
st.markdown(f"""
    <div class="info-box">
        <p class="info-text">👤 <span class="info-highlight">Fundador y Director:</span> <a href="{url_pedro_perfil}" target="_blank" class="founder-link">Pedro Elsrdelsur</a></p>
        <p class="info-text">👥 <span class="info-highlight">Subdirector:</span> Raúl Lizarraga</p>
    </div>
""", unsafe_allow_html=True)

# --- BOTONES DE ENLACES ---
st.markdown(f'<a href="{url_descarga_app}" target="_blank" class="custom-btn btn-app">⬇️ Descargar App Oficial</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{url_facebook}" target="_blank" class="custom-btn btn-fb">Página Oficial de Facebook</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{url_youtube}" target="_blank" class="custom-btn btn-yt">Canal de YouTube</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
