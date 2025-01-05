import os

from fastapi import UploadFile


async def save_img(image: UploadFile) -> str:
    new_path = os.path.join(os.path.abspath('temp'), image.filename)
    with open(new_path, 'wb') as out_file:
        content = await image.read()
        out_file.write(content)
    return new_path


async def remove_img(image: str) -> None:
    try:
        os.remove(image)
    except:
        pass
