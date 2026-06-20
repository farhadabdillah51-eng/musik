from moviepy.editor import (
VideoFileClip,
TextClip,
CompositeVideoClip,
AudioFileClip
)

import os

def render_typography_video(
video_path,
audio_path,
lyrics_data,
output_path="output/final_video.mp4"
):

```
os.makedirs(
    "output",
    exist_ok=True
)

background = VideoFileClip(
    video_path
)

audio = AudioFileClip(
    audio_path
)

clips = [background]

for item in lyrics_data:

    txt = TextClip(
        item["text"],
        fontsize=70,
        color="white",
        stroke_color="black",
        stroke_width=2
    )

    txt = (
        txt
        .set_start(item["start"])
        .set_end(item["end"])
        .set_position(
            ("center","center")
        )
    )

    clips.append(txt)

final = CompositeVideoClip(
    clips
)

final = final.set_audio(
    audio
)

final.write_videofile(
    output_path,
    codec="libx264",
    audio_codec="aac",
    fps=30
)

return output_path
```
