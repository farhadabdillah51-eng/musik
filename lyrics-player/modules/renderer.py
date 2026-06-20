```python
from moviepy import (
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
            text=item["text"],
            font_size=70,
            color="white",
            stroke_color="black",
            stroke_width=2,
            method="caption",
            size=(
                int(background.w * 0.8),
                None
            )
        )

        txt = (
            txt
            .with_start(item["start"])
            .with_end(item["end"])
            .with_position(
                ("center", "center")
            )
        )

        clips.append(txt)

    final = CompositeVideoClip(
        clips,
        size=background.size
    )

    final = final.with_audio(
        audio
    )

    final.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )

    return output_path
```

