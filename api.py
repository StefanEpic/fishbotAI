from typing import Dict

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from neuro import get_float_coords
from utils import save_img, remove_img

app = FastAPI(title="Wow fishing")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"], )


@app.post("/get_coords", response_model=Dict[str, float])
async def get_coords(image: UploadFile) -> Dict[str, float]:
    img_path = await save_img(image=image)
    result = await get_float_coords(image=img_path)
    await remove_img(image=img_path)
    return result
