import streamlit as st
import os

st.set_page_config(
page_title="AI Typography Video Generator",
page_icon="🎵",
layout="wide"
)

st.title("🎵 AI Typography Video Generator")

os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)

audio_file = st.file_uploader(
"Upload MP3",
type=["mp3"]
)

video_file = st.file_uploader(
"Upload Background Video",
type=["mp4", "mov", "avi"]
)

if audio_file is not None:
audio_path = os.path.join(
"uploads",
audio_file.name
)

```
with open(audio_path, "wb") as f:
    f.write(audio_file.read())

st.success(
    f"MP3 berhasil diupload: {audio_file.name}"
)
```

if video_file is not None:
video_path = os.path.join(
"uploads",
video_file.name
)

```
with open(video_path, "wb") as f:
    f.write(video_file.read())

st.success(
    f"Video berhasil diupload: {video_file.name}"
)
```

if audio_file is not None and video_file is not None:

```
st.success(
    "Semua file berhasil diupload."
)

if st.button(
    "🎬 Generate Typography Video"
):
    st.info(
        "Fitur renderer belum diaktifkan."
    )
```

else:

```
st.info(
    "Upload MP3 dan Video terlebih dahulu."
)
```
