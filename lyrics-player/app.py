import streamlit as st
import os

# Konfigurasi halaman

st.set_page_config(
page_title="AI Typography Video Generator",
page_icon="🎵",
layout="wide"
)

# CSS

st.markdown("""

<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b,#020617);
}

.title {
    text-align:center;
    color:white;
    font-size:3rem;
    font-weight:bold;
    margin-bottom:20px;
}
</style>

""", unsafe_allow_html=True)

# Judul

st.markdown(
'<div class="title">🎵 AI Typography Video Generator</div>',
unsafe_allow_html=True
)

# Folder

os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Upload MP3

audio_file = st.file_uploader(
"Upload MP3",
type=["mp3"]
)

# Upload Video

video_file = st.file_uploader(
"Upload Background Video",
type=["mp4", "mov", "avi"]
)

# Simpan MP3

if audio_file is not None:

```
audio_path = os.path.join(
    "uploads",
    audio_file.name
)

with open(audio_path, "wb") as f:
    f.write(audio_file.read())

st.success(
    f"MP3 berhasil diupload: {audio_file.name}"
)
```

# Simpan Video

if video_file is not None:

```
video_path = os.path.join(
    "uploads",
    video_file.name
)

with open(video_path, "wb") as f:
    f.write(video_file.read())

st.success(
    f"Video berhasil diupload: {video_file.name}"
)
```

# Status

if audio_file is not None and video_file is not None:

```
st.success(
    "Semua file berhasil diupload."
)

if st.button(
    "🎬 Generate Typography Video"
):
    st.info(
        "Fitur renderer akan ditambahkan berikutnya."
    )
```

else:

```
st.info(
    "Upload MP3 dan Video terlebih dahulu."
)
```
