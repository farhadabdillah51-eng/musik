```python
from faster_whisper import WhisperModel

# Model dimuat sekali saja
model = WhisperModel(
    "small",
    compute_type="int8"
)

def transcribe_audio(audio_path):

    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        word_timestamps=True
    )

    results = []

    for segment in segments:

        words = []

        if segment.words:

            for word in segment.words:

                words.append({
                    "word": word.word.strip(),
                    "start": round(
                        word.start, 2
                    ),
                    "end": round(
                        word.end, 2
                    )
                })

        results.append({
            "start": round(
                segment.start, 2
            ),
            "end": round(
                segment.end, 2
            ),
            "text": segment.text.strip(),
            "words": words
        })

    return results
```

