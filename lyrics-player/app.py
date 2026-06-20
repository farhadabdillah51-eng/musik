```python
import streamlit as st
import tempfile
import os

from modules.transcriber import transcribe_audio

st.set_page_config(
    page_title="AI Typography Video Generator",
    page_icon="🎵",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.stApp{
    background:
    linear-gradient(
    135deg,
    #0f172a,
    #1e293b,
    #020617);
}

.title{
    text-align:center;
    color:white;
    font-size:4rem;
    font-weight:800;
}

.glass{
    background:
    rgba(255,255,255,.08);

    backdrop-filter:
    blur(20px);

    border:
    1px solid rgba(
    255,255,255,.15);

    border-radius:
    25px;

    padding:
    25px;

    margin-bottom:
    20px;
}

.stButton>button{

    width:100%;

    border-radius:
    999px;

    transition:
    .3s;

}

.stButton>button:hover{

    transform:
    scale(1.04);

}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="title">
    🎵 AI Typography Generator
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

audio_file = st.file_uploader(
    "Upload MP3",
    type=["mp3"]
)

video_file = st.file_uploader(
    "Upload Background Video",
    type=["mp4","mov","avi"]
)

if audio_file:

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    audio_path = os.path.join(
        "uploads",
        audio_file.name
    )

    with open(
        audio_path,
        "wb"
    ) as f:

        f.write(
            audio_file.read()
        )

    st.success(
        "MP3 berhasil diupload"
    )

if video_file:

    video_path = os.path.join(
        "uploads",
        video_file.name
    )

    with open(
        video_path,
        "wb"
    ) as f:

        f.write(
            video_file.read()
        )

    st.success(
        "Video berhasil diupload"
    )

if audio_file:

    if st.button(
        "🎤 Generate Lyrics"
    ):

        with st.spinner(
            "Whisper sedang bekerja..."
        ):

            result = transcribe_audio(
                audio_path
            )

        st.session_state[
            "lyrics"
        ] = result

        st.success(
            "Transkripsi selesai"
        )

if "lyrics" in st.session_state:

    st.subheader(
        "Hasil Transkripsi"
    )

    for item in st.session_state[
        "lyrics"
    ]:

        st.write(
            f"[{item['start']:.2f}s] {item['text']}"
        )

if (
    "lyrics" in st.session_state
    and video_file
):

    if st.button(
        "🎬 Generate Typography Video"
    ):

        st.info(
            "Renderer akan dibuat pada file berikutnya"
        )
```
