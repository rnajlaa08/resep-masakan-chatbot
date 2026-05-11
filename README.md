# 🍳 Resep Masakan Kamu

Chatbot asisten memasak berbasis AI menggunakan **Google Gemini** dan **Streamlit**.

## ✨ Fitur

- 💬 Chat interaktif dalam Bahasa Indonesia
- 🍽️ Resep lengkap dengan bahan dan langkah memasak
- 🎛️ Filter gaya memasak dan tingkat kesulitan
- 🔒 API Key aman (diinput langsung di sidebar, tidak tersimpan)
- 🗑️ Reset percakapan kapan saja

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/rnajlaa08/resep-masakan-chatbot.git
cd resep-masakan-chatbot
```

### 2. Install Dependensi

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

### 4. Dapatkan API Key

Dapatkan Google AI API Key gratis di [https://aistudio.google.com](https://aistudio.google.com), lalu masukkan di sidebar aplikasi.

## ☁️ Deploy ke Streamlit Cloud

1. Push repository ini ke GitHub
2. Buka [https://share.streamlit.io](https://share.streamlit.io)
3. Klik **New app** → pilih repository ini
4. Set **Main file path** ke `app.py`
5. Klik **Deploy!**

## 🛠️ Teknologi

- [Streamlit](https://streamlit.io) — Framework web app Python
- [Google Gemini API](https://aistudio.google.com) — Model LLM dari Google
- [google-genai](https://pypi.org/project/google-genai/) — Python SDK untuk Gemini

## 📁 Struktur File

```
resep-masakan-chatbot/
├── app.py                  # File utama Streamlit
├── requirements.txt        # Dependensi Python
├── .streamlit/
│   └── config.toml         # Konfigurasi tema Streamlit
└── README.md               # Dokumentasi ini
```
