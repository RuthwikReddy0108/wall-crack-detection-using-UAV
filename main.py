from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import shutil
# from subprocess import call
import os

app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    out_file_path=f'Uploads/{file.filename}'
    with open(out_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    fileN=f'Uploads/{file.filename}'
    os.system(f"yolo task=detect mode=predict model=best.pt conf=0.7 source={fileN}")
    return {"filename": file.filename}
