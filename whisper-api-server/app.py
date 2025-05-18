from fastapi import FastAPI, File, UploadFile
from faster_whisper import WhisperModel

app = FastAPI()
model = WhisperModel("base")  # or "medium", "large", etc.

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    audio_data = await file.read()
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_data)

    segments, info = model.transcribe("temp_audio.mp3")
    text = " ".join(segment.text for segment in segments)
    return {"transcription": text}
