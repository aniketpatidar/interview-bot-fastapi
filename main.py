from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.post("/talk")
async def post_audio(file: UploadFile):
  transcribe_audio(file)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

def transcribe_audio(file):
  audio_file= open(file.filename, "rb")
  transcription = openai.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
  )
  print(transcription.text)
  return {"message": "Audio Transcribed"}

# 1. Send in audio, and have it transcribed
# 2. Sen it to chatgpt and get a response
# 3. We wanted to save the chat history to send back and forth for context
