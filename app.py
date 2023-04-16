from easynmt import EasyNMT
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Union, List
from fastapi import FastAPI, HTTPException, Query, Request

model = EasyNMT('opus-mt')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def translate_get(target_lang: str, text: List[str] = Query([]), source_lang: Optional[str] = None):
  return model.translate(text, target_lang=target_lang, source_lang=source_lang)

@app.post("/")
async def translate_post(request: Request):
    data = await request.json()
    return translate_get(**data)

uvicorn.run(app, port=8000)
