# coding: utf-8
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import cv2
import webbrowser
import sys
import sounddevice as sd
import numpy as np

v = tk.Tk()
v.title("MUNDYSTREEM ULTRA PRO v5.1")
v.geometry("1280x725")
v.configure(bg="#0c1214")

ar = {}
vr = {}
v_cap = None
ff_process = None
repro = False
s_mic = None

M_FILE = os.path.expanduser("~/Documents/mundystreem_memoria.txt")
DB_FILE = os.path.expanduser("~/Documents/mundystreem_url_db.txt")

def guardar_m():
    try:
        with open(M_FILE, "w", encoding="utf-8") as f:
            for n, r in ar.items(): f.write(f"A|{n}|{r}\n")
            for n, r in vr.items(): f.write(f"V|{n}|{r}\n")
    except: pass

def cargar_m():
    if os.path.exists(M_FILE):
        try:
            with open(M_FILE, "r", encoding="utf-8") as f:
                for l in f:
                    p = l.strip().split("|")
                    if len(p) == 3:
                        n, r = p, p
                        if p == "A" and lst_a.size() < 50: ar[n] = r; lst_a.insert(tk.END, n)
                        if p == "V" and lst_v.size() < 50: vr[n] = r; lst_v.insert(tk.END, n)
        except: pass
def encender_camara_local():
    global v_cap, repro
    try:
        if v_cap is not None: v_cap.release()
        # SOFTWARE DE TU FOTO: Resolucion real 1280x720 de largo
        v_cap = cv2.VideoCapture(0)
        v_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        v_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        if not v_cap.isOpened():
            messagebox.showerror("Error", "No se detecto camara conectada.")
            return
        repro = True
        frame_loop_live()
        lbl_trans.config(text="● CAMARA LOCAL OK", fg="#00ff00")
    except:
        messagebox.showerror("Error", "Fallo al abrir hardware local.")

def conectar_ninja_en_panel():
    url_ninja = txt_url_ninja.get().strip()
    if not url_ninja or "Pegue" in url_ninja:
        messagebox.showwarning("MundyStreem", "Por favor pegue el link de captura de Ninja arriba.")
        return
    # TRANSMISION DIRECTA: Fuerza a tu Windows a abrir el Chrome al instante
    try:
        webbrowser.open(url_ninja)
        lbl_trans.config(text="● ENLACE NINJA OK", fg="#00ff00")
        monitor_cam.config(text="📡 SEÑAL ACTIVA EN INTERNET\n\nAbriendo la señal de tu invitado en Google Chrome...", fg="#00FFCC")
    except:
        messagebox.showerror("Error", "No se pudo inyectar el navegador.")

def lanzar_live_redes():
    global ff_process, v_cap, repro
    clave = txt_url_fb.get().strip()
    
    if not clave or "rtmp://" not in clave:
        messagebox.showwarning("Error", "Pega la clave RTMP completa de Facebook")
        return
    
    if not v_cap or not v_cap.isOpened():
        messagebox.showwarning("Error", "Abre primero la cámara")
        return
    
     # ✅ CONFIGURACION OPTIMIZADA PARA FACEBOOK - SIN COMPLICACIONES
    cmd = ["ffmpeg", "-y", "-f", "rawvideo",
        "-vcodec", "rawvideo", "-pix_fmt", "bgr24",
        "-s", "1280x720", "-r", "30", "-i", "-",
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-preset", "ultrafast", "-tune", "zerolatency",
        "-b:v", "2500k", "-maxrate", "2500k", "-bufsize", "5000k",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-f", "flv", clave]
        "-f", "flv", clave]
    
    try:
        ff_process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        repro = True
        lbl_trans.config(text="● TRANSMITIENDO", fg="#00ff00")
        messagebox.showinfo("MundyStreem", "✅ Señal enviada a Facebook con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo iniciar: {e}")

def frame_loop_live():
    global v_cap, repro
    if repro and v_cap and v_cap.isOpened():
        ret, frame = v_cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            # TU TITULO MASTER ORIGINAL DE LA FOTO INTACTO
            cv2.putText(frame, "MUNDYSTREEM - RADIO MUNDY CHIAPS EN VIVO", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
            f_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(f_rgb).resize((560, 240), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(image=img)
            monitor_cam.config(image=img_tk)
            monitor_cam.image = img_tk
            v.after(33, frame_loop_live)

def open_mic():
    global s_mic
    if s_mic is None:
        try:
            s_mic = sd.Stream(samplerate=44100, channels=1, callback=lambda i,o,f,t,s: o.copy(i))
            s_mic.start()
            lbl_mic.config(text="● MIC ON", fg="#00ff00")
        except: pass

def close_mic():
    global s_mic
    if s_mic is not None:
        s_mic.stop(); s_mic.close(); s_mic = None
        lbl_mic.config(text="● MUTED", fg="#b71c1c")
def add_aud():
    for r in filedialog.askopenfilenames(filetypes=[("MP3", "*.mp3")]):
        n = os.path.basename(r); lst_a.insert(tk.END, n); ar[n] = r; guardar_m()

def play_aud():
    try: os.system(f'start cmd /c start /min "" "{ar[lst_a.get(lst_a.curselection())]}"')
    except: pass

def stop_aud():
    os.system("taskkill /f /im Microsoft.Media.Player.exe >nul 2>&1")
    os.system("taskkill /f /im wmplayer.exe >nul 2>&1")

def add_vid():
    for r in filedialog.askopenfilenames(filetypes=[("Videos MP4", "*.mp4")]):
        n = os.path.basename(r); lst_v.insert(tk.END, n); vr[n] = r; guardar_m()

# MAQUETACIÓN EN COLUMNAS IDÉNTICA A TU FOTO ORIGINAL
f_central = tk.Frame(v, bg="#0c1214")
f_central.pack(fill="both", expand=True, padx=10, pady=10)

# COLUMN 1. TRANSMISION
c1 = tk.LabelFrame(f_central, text=" TRANSMISION ", fg="#ffffff", bg="#0c1214", font=("Arial", 9, "bold"))
c1.pack(side="left", fill="both", padx=5, expand=True)
lbl_trans = tk.Label(c1, text="● EN ESPERA", fg="#b71c1c", bg="#0c1214", font=("Arial", 9, "bold"))
lbl_trans.pack(pady=2)
tk.Label(c1, text="PEGA TU LLAVE RTMPS:", fg="#00ffcc", bg="#0c1214", font=("Arial", 8)).pack()
txt_url_fb = tk.Entry(c1, bg="#13131a", fg="#ffffff", font=("Arial", 8), bd=1)
txt_url_fb.pack(fill="x", padx=5, pady=2)
txt_url_fb.insert(0, "rtmps://://facebook.com")

tk.Button(c1, text="📷 PROBAR MI IMAGEN", command=encender_camara_local, bg="#2c3e50", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c1, text="🍏 ESTUDIO VIRTUAL", bg="#27ae60", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c1, text="📺 SET PAISAJE", bg="#2980b9", font=("Arial", 8, "bold"), fg="white").pack(fill="x", padx=5, pady=3)
tk.Button(c1, text="📣 TRANSMITIR", command=lanzar_live_redes, bg="#16a085", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)

# LA CASILLA DE INYECCIÓN PARA SU INVITADO NINJA ABAJO
tk.Label(c1, text="LINK DE CAPTURA NINJA:", fg="#ff00ff", bg="#0c1214", font=("Arial", 8, "bold")).pack(pady=(5,0))
txt_url_ninja = tk.Entry(c1, bg="#13131a", fg="#ffffff", font=("Arial", 8), bd=1)
txt_url_ninja.pack(fill="x", padx=5, pady=2)
txt_url_ninja.insert(0, "Pegue aqui el link de captura...")
tk.Button(c1, text="🚀 ENLAZAR INVITADO", command=conectar_ninja_en_panel, bg="#8e44ad", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=2)

# COLUMN 2. MICROFONO
c2 = tk.LabelFrame(f_central, text=" MICROFONO ", fg="#ffffff", bg="#0c1214", font=("Arial", 9, "bold"))
c2.pack(side="left", fill="both", padx=5, expand=True)
lbl_mic = tk.Label(c2, text="● MUTED", fg="#b71c1c", bg="#0c1214", font=("Arial", 9, "bold"))
lbl_mic.pack(pady=2)
tk.Button(c2, text="ABRIR MIC", command=open_mic, bg="#27ae60", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c2, text="MUTEAR VOZ", command=close_mic, bg="#c0392b", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c2, text="AGUDOS/BRILLO", bg="#7f8c8d", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c2, text="COMPRESOR", bg="#7f8c8d", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c2, text="REVERBERACION", bg="#7f8c8d", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)

# COLUMN 3. AUDIO MP3
c3 = tk.LabelFrame(f_central, text=" AUDIO MP3 ", fg="#ffffff", bg="#0c1214", font=("Arial", 9, "bold"))
c3.pack(side="left", fill="both", padx=5, expand=True)
tk.Label(c3, text="● STOP", fg="#b71c1c", bg="#0c1214", font=("Arial", 9, "bold")).pack(pady=2)
tk.Button(c3, text="CAPTAR MP3", command=add_aud, bg="#2c3e50", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
lst_a = tk.Listbox(c3, bg="#1a252f", fg="#ffffff", font=("Arial", 8), height=8)
lst_a.pack(fill="x", padx=5, pady=2)
tk.Button(c3, text="AL AIRE", command=play_aud, bg="#27ae60", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c3, text="SILENCIAR", command=stop_aud, bg="#c0392b", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)

# COLUMN 4. VIDEOS MP4
c4 = tk.LabelFrame(f_central, text=" VIDEOS MP4 ", fg="#ffffff", bg="#0c1214", font=("Arial", 9, "bold"))
c4.pack(side="left", fill="both", padx=5, expand=True)
tk.Label(c4, text="● OFF", fg="#b71c1c", bg="#0c1214", font=("Arial", 9, "bold")).pack(pady=2)
tk.Button(c4, text="CAPTAR MP4", command=add_vid, bg="#2c3e50", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
lst_v = tk.Listbox(c4, bg="#1a252f", fg="#ffffff", font=("Arial", 8), height=8)
lst_v.pack(fill="x", padx=5, pady=2)
tk.Button(c4, text="VER IMAGEN", bg="#e67e22", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c4, text="ESCUCHAR", bg="#2980b9", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c4, text="SILENCIAR", bg="#7f8c8d", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)
tk.Button(c4, text="APAGAR TODO", command=v.destroy, bg="#c0392b", fg="white", font=("Arial", 8, "bold")).pack(fill="x", padx=5, pady=3)

# COLUMN 5. MONITOR INTEGRADO (EL RECUADRO DE TU SEÑAL)
c5 = tk.LabelFrame(f_central, text=" MONITOR INTEGRADO ", fg="#ffffff", bg="#0c1214", font=("Arial", 9, "bold"))
c5.pack(side="left", fill="both", padx=5, expand=True)
monitor_cam = tk.Label(c5, text="Espera Camara", bg="#000000", fg="#00FFCC", font=("Arial", 11, "bold"), wrap=220)
monitor_cam.pack(fill="both", expand=True, padx=5, pady=5)

tk.Label(v, text="Autor Legitimo: Irineo Pedro Hernandez Hernandez", font=("Arial", 8, "bold"), fg="#7f8c8d", bg="#0a0a0d").pack(side="bottom", pady=2)

def abrir_link_ninja(): webbrowser.open("https://vdo.ninja")
tk.Button(v, text="🌐 ABRIR CABINA EXTERNA NINJA", command=abrir_link_ninja, bg="#111111", fg="#ff00ff", font=("Arial", 7, "bold")).pack(side="bottom", fill="x")

cargar_m(); v.mainloop()
