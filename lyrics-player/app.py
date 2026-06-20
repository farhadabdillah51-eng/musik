import streamlit as st
import re
import base64

st.set_page_config(
    page_title="Lyrics Typography Player",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 Lyrics Typography Player")

uploaded_audio = st.file_uploader(
    "Upload Lagu MP3",
    type=["mp3"]
)

lyrics_text = st.text_area(
    "Masukkan Lirik (Format LRC)",
    height=250,
    value="""[00:00] Aku yang dulu
[00:05] Bukanlah yang sekarang
[00:10] Kini ku telah kembali
[00:15] Tak seperti yang dahulu"""
)

if uploaded_audio:

    audio_bytes = uploaded_audio.read()

    audio_base64 = base64.b64encode(audio_bytes).decode()

    pattern = r"\[(\d+):(\d+)\]\s*(.*)"

    lyrics = []

    for line in lyrics_text.splitlines():

        match = re.match(pattern, line)

        if match:

            minute = int(match.group(1))
            second = int(match.group(2))
            text = match.group(3)

            total_seconds = minute * 60 + second

            lyrics.append({
                "time": total_seconds,
                "text": text
            })

    lyrics_js = str(lyrics).replace("'", '"')

    html_code = f"""
    <style>

    body {{
        margin:0;
        padding:0;
        background:black;
        overflow:hidden;
    }}

    #container {{
        width:100%;
        text-align:center;
        margin-top:40px;
    }}

    #lyrics {{
        color:white;
        font-size:60px;
        font-weight:bold;
        min-height:120px;
        margin-top:50px;
        text-shadow:
        0 0 10px white,
        0 0 20px white;
        transition:all .3s ease;
    }}

    audio {{
        width:80%;
        margin-top:30px;
    }}

    </style>

    <div id="container">

        <audio id="audio" controls>
            <source src="data:audio/mp3;base64,{audio_base64}">
        </audio>

        <div id="lyrics">
            Tekan Play
        </div>

    </div>

    <script>

    const lyrics = {lyrics_js};

    const audio =
        document.getElementById("audio");

    const lyricBox =
        document.getElementById("lyrics");

    audio.addEventListener(
        "timeupdate",
        () => {{

            const current =
                audio.currentTime;

            for(let i=0;i<lyrics.length;i++){{

                const currentLine =
                    lyrics[i];

                const nextLine =
                    lyrics[i+1];

                if(
                    current >= currentLine.time &&
                    (
                        !nextLine ||
                        current < nextLine.time
                    )
                ){{
                    lyricBox.innerHTML =
                        currentLine.text;
                }}
            }}

        }}
    );

    </script>
    """

    st.components.v1.html(
        html_code,
        height=500,
        scrolling=False
    )

else:
    st.info("Upload MP3 terlebih dahulu")
