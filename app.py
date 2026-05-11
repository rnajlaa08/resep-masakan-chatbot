import streamlit as st
from google import genai
 
# ── Konfigurasi Halaman ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="Resep Masakan Kamu",
    page_icon="🍳",
    layout="centered",
)
 
# ── Judul Utama ───────────────────────────────────────────────────────────────
st.title("🍳 Resep Masakan Kamu")
st.caption("Asisten masak pintarmu — tanya resep apa saja, dari masakan rumahan hingga hidangan spesial!")
 
# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Pengaturan")
 
    api_key = st.text_input(
        "Google AI API Key",
        type="password",
        placeholder="Masukkan API Key kamu...",
        help="Dapatkan API Key gratis di https://aistudio.google.com",
    )
 
    st.divider()
 
    st.subheader("🎛️ Preferensi Masakan")
 
    gaya_masak = st.selectbox(
        "Gaya Memasak",
        ["Semua Gaya", "Masakan Rumahan Sederhana", "Masakan Restaurant", "Masakan Sehat", "Masakan Cepat (< 30 menit)"],
    )
 
    tingkat_kesulitan = st.selectbox(
        "Tingkat Kesulitan",
        ["Semua Level", "Pemula", "Menengah", "Mahir"],
    )
 
    st.divider()
 
    if st.button("🗑️ Reset Percakapan", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.rerun()
 
    st.divider()
    st.markdown(
        """
        **💡 Contoh Pertanyaan:**
        - Resep ayam goreng crispy?
        - Cara membuat nasi goreng spesial?
        - Apa saja bahan untuk rendang?
        - Bagaimana cara membuat kue bolu?
        - Resep dengan bahan tahu dan tempe?
        """
    )
 
# ── System Prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = f"""
Kamu adalah asisten memasak yang ramah dan berpengalaman bernama "Chef AI". 
Kamu hanya membahas topik seputar masakan, resep, bahan makanan, teknik memasak, dan tips dapur.
 
Preferensi pengguna saat ini:
- Gaya memasak: {gaya_masak}
- Tingkat kesulitan yang diinginkan: {tingkat_kesulitan}
 
Aturan penting:
1. Selalu gunakan Bahasa Indonesia yang ramah dan mudah dipahami.
2. Jika pengguna bertanya di luar topik masakan, dengan sopan arahkan kembali ke topik masakan.
3. Saat memberikan resep, selalu sertakan:
   - Bahan-bahan (dengan takaran yang jelas)
   - Langkah-langkah memasak (nomor urut)
   - Tips atau variasi jika ada
4. Sesuaikan resep dengan preferensi gaya memasak dan tingkat kesulitan pengguna.
5. Gunakan emoji makanan sesekali agar percakapan lebih menarik.
"""
 
# ── Inisialisasi Session State ────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
 
# ── Validasi API Key ──────────────────────────────────────────────────────────
if not api_key:
    st.info("👈 Masukkan **Google AI API Key** di sidebar untuk mulai menggunakan chatbot.", icon="🔑")
    st.stop()
 
# ── Pesan Sambutan ────────────────────────────────────────────────────────────
if len(st.session_state.messages) == 0:
    welcome = "Halo! 👋 Saya Chef AI, asisten memasak kamu. Mau masak apa hari ini? Tanyakan resep, bahan, atau tips memasak apa saja — saya siap membantu! 🍳"
    st.session_state.messages.append({"role": "assistant", "content": welcome})
 
# ── Tampilkan Riwayat Chat ────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
 
# ── Input Pengguna ────────────────────────────────────────────────────────────
prompt = st.chat_input("Tanyakan resep atau tips memasak di sini...")
 
if prompt:
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
 
    # Buat client & chat BARU setiap ada pesan (hindari client closed error)
    with st.chat_message("assistant"):
        with st.spinner("Chef AI sedang menyiapkan jawaban... 👨‍🍳"):
            try:
                client = genai.Client(api_key=api_key)
 
                # Bangun ulang riwayat percakapan untuk konteks
                history = []
                for m in st.session_state.chat_history:
                    history.append(m)
 
                chat = client.chats.create(
                    model="gemini-2.0-flash",
                    config={"system_instruction": SYSTEM_PROMPT},
                    history=history,
                )
 
                response = chat.send_message(prompt)
                answer = response.text if hasattr(response, "text") else str(response)
 
                # Simpan ke history untuk konteks percakapan berikutnya
                st.session_state.chat_history.append({
                    "role": "user",
                    "parts": [{"text": prompt}]
                })
                st.session_state.chat_history.append({
                    "role": "model",
                    "parts": [{"text": answer}]
                })
 
            except Exception as e:
                answer = f"❌ Terjadi kesalahan: {e}\n\nPastikan API Key kamu benar dan coba lagi."
 
        st.markdown(answer)
 
    st.session_state.messages.append({"role": "assistant", "content": answer})
