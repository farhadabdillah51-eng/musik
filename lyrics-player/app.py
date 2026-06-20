import streamlit as st
import tempfile
from faster_whisper import WhisperModel

st.set_page_config(
    page_title="AI Lyrics Typography",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 AI Lyrics Typography")

uploaded_audio = st.file_uploader(
    "Upload Lagu MP3",
    type=["mp3"]
)

if uploaded_audio:

    st.info("Menyimpan file...")

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    ) as tmp:

        tmp.write(uploaded_audio.read())
        audio_path = tmp.name

    st.info("Memuat model Whisper...")

    model = WhisperModel(
        "tiny",
        compute_type="int8"
    )

    st.info("Mentranskripsi lagu...")

    segments, info = model.transcribe(
        audio_path,
        beam_size=5
    )

    lyrics_data = []

    for segment in segments:

        lyrics_data.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": segment.text
        })

    st.success("Transkripsi selesai!")

    for row in lyrics_data:

        st.markdown(
            f"""
            **[{row['start']}s]**
            {row['text']}
            """
        )
