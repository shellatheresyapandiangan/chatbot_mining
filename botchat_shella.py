import streamlit as st
from together import Together

# Konfigurasi model
MODEL_CONFIG = {
    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
}

# Fungsi untuk memanggil model
def call_model(prompt, api_key, max_tokens=4096, temperature=0.6, top_p=0.95, top_k=50, repetition_penalty=1.5):
    client = Together(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model=MODEL_CONFIG["model"],
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            stream=True
        )
        return "".join(token.choices[0].delta.content for token in response if hasattr(token, 'choices'))
    except (IndexError, KeyError, TypeError, AttributeError):
        return "Terjadi kesalahan dalam mendapatkan respons."

# Konfigurasi halaman
st.set_page_config(page_title="LLM with Shella Pandiangan", page_icon="🦙", layout="wide")

# Sidebar API Key dan Pengaturan Model
st.sidebar.header("Konfigurasi API")
st.sidebar.markdown("**Key API di-generate sendiri:** [Dapatkan API Key](https://api.together.ai/settings/api-keys)")
st.sidebar.markdown("**Kalau tidak bisa generate API sendiri, berikut ini sample API:** `4136908e38206c232c380542563d986ccd638a22ab04d3326ada29f59ee91cbe` dan paste di box bawah ini")
api_key = st.sidebar.text_input("Masukkan API Key Together AI:", type="password")

st.sidebar.header("Pengaturan Model")
max_tokens = st.sidebar.slider("Output Length", min_value=256, max_value=8192, value=4096)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.6)
top_p = st.sidebar.slider("Top-P", min_value=0.0, max_value=1.0, value=0.95)
top_k = st.sidebar.slider("Top-K", min_value=0, max_value=100, value=50)
repetition_penalty = st.sidebar.slider("Repetition Penalty", min_value=0.5, max_value=2.0, value=1.5)

# Header
st.markdown('<div class="header-title">LLM with Shella Pandiangan 🦙</div>', unsafe_allow_html=True)

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
                result = call_model(user_input, api_key, max_tokens, temperature, top_p, top_k, repetition_penalty)
            st.success("Berhasil mendapatkan hasil!")
            st.subheader("Hasil:")
            st.write(result)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Dibuat oleh Shella Theresya Pandiangan menggunakan LLM, Semoga Membantu!.</div>', unsafe_allow_html=True)
