import streamlit as st
import requests
import os

# Konfigurasi model
MODEL_CONFIG = {
    "model": "deepseek-chat",
    "api_url": "https://api.together.xyz/v1/chat/completions"
}

# Fungsi untuk memanggil model

def call_model(prompt, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": MODEL_CONFIG["model"],
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512
    }
    try:
        response = requests.post(MODEL_CONFIG["api_url"], json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "No response from model")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Konfigurasi halaman
st.set_page_config(page_title="LLM with Shella Pandiangan", page_icon="🦙", layout="wide")

# Sidebar API Key
st.sidebar.header("Konfigurasi API")
api_key = st.sidebar.text_input("Masukkan API Key Together AI:", type="password")

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
    Aplikasi ini dibuat menggunakan **DeepSeek** untuk membantu Anda mendapatkan jawaban cerdas dari AI.
    
    Dibuat oleh **Shella Theresya Pandiangan**.
    
    [LinkedIn Shella Theresya Pandiangan](https://id.linkedin.com/in/shellatheresyapandiangan)
""", unsafe_allow_html=True)

# Menampilkan gambar kecil di bawah About This App
st.sidebar.image("shel.JPG", caption="Shella Pandiangan", width=80)

# Input pengguna
txt_container = st.container()
with txt_container:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    user_input = st.text_area("Masukkan prompt:", height=150, placeholder="Tulis pertanyaan Anda di sini...")
    if st.button("Generate 🚀", key="generate_button", help="Klik untuk menjalankan AI model"):
        if user_input.strip() == "":
            st.warning("Silakan masukkan prompt terlebih dahulu.")
        elif not api_key:
            st.warning("Silakan masukkan API Key di sidebar.")
        else:
            with st.spinner("Memproses..."):
                result = call_model(user_input, api_key)
            st.success("Berhasil mendapatkan hasil!")
            st.subheader("Hasil:")
            st.write(result)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Dibuat oleh Shella Theresya Pandiangan menggunakan Streamlit dan model DeepSeek.</div>', unsafe_allow_html=True)
