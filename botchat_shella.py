import streamlit as st
import requests

# Konfigurasi model
MODEL_CONFIG = {
    "model": "deepseek-r1:1.5b",
    "provider": "ollama",
    "apiKey": "",  # Isi dengan API key jika diperlukan
    "title": "LLM with Shella Pandiangan"
}

# Endpoint API model
API_URL = "http://localhost:11434/api/generate"

# Fungsi untuk memanggil model
def call_model(prompt):
    headers = {"Content-Type": "application/json"}
    data = {"model": MODEL_CONFIG["model"], "prompt": prompt, "stream": False}
    try:
        response = requests.post(API_URL, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response from model")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Konfigurasi halaman
st.set_page_config(page_title="LLM with Shella Pandiangan", page_icon="🦙", layout="wide")

# Custom CSS untuk tampilan profesional
st.markdown("""
    <style>
        body {
            background-color: #121212 !important;
            color: #FFFFFF;
            font-family: 'Segoe UI', sans-serif;
        }

        [data-testid="stSidebar"] {
            background-color: #1E1E1E !important;
            color: #FFFFFF;
        }

        .header-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #FFD700;
            margin-top: 20px;
        }

        .input-card {
            background: #252525;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(255, 215, 0, 0.3);
            margin: 30px auto;
            width: 50%;
        }

        .custom-button {
            background-color: #FFD700;
            color: black;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .custom-button:hover {
            background-color: #FFC107;
        }

        .footer {
            text-align: center;
            color: #AAAAAA;
            font-size: 14px;
            margin-top: 30px;
        }

        .running-text {
            white-space: nowrap;
            overflow: hidden;
            box-sizing: border-box;
            animation: marquee 10s linear infinite;
            font-size: 20px;
            color: #FFD700;
            margin-top: 10px;
            text-align: center;
        }
        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-title">LLM with Shella Pandiangan 🦙</div>', unsafe_allow_html=True)

# Running Text
st.markdown('<div class="running-text">🚀 Selamat datang di AI Chatbot berbasis DeepSeek! Buat pertanyaan dan temukan jawabannya! 🌟</div>', unsafe_allow_html=True)

# Sidebar About This App
st.sidebar.markdown("""
    ## About This App
    Aplikasi ini dibuat menggunakan **Model LLM** untuk membantu Anda mendapatkan jawaban cerdas dari AI.
    
    Dibuat oleh **Shella Theresya Pandiangan**.
    
    [LinkedIn Shella Theresya Pandiangan](https://id.linkedin.com/in/shellatheresyapandiangan)
""", unsafe_allow_html=True)

# Menampilkan gambar kecil di bawah About This App
st.sidebar.image("shel.jpg", caption="Shella Pandiangan", width=80)

# Input pengguna
txt_container = st.container()
with txt_container:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    user_input = st.text_area("Coba tanyakan apa saja:", height=150, placeholder="Tulis pertanyaan Anda di sini...")
    if st.button("Generate 🚀", key="generate_button", help="Klik untuk menjalankan AI model"):
        if user_input.strip() == "":
            st.warning("Silakan masukkan prompt terlebih dahulu.")
        else:
            with st.spinner("Memproses..."):
                result = call_model(user_input)
            st.success("Berhasil mendapatkan hasil!")
            st.subheader("Hasil:")
            st.write(result)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Dibuat oleh Shella Theresya Pandiangan menggunakan salah satu model LLM.</div>', unsafe_allow_html=True)