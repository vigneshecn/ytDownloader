import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World1"}


@app.get("/music/single/{yt_link}")
async def getMusicSingle(yt_link: str ="fvUmrVnqLV0"):
    current_dir = os.getcwd()
    LOCAL_PATH = os.path.join(current_dir, "downloads")
    #LOCAL_PATH = "./downloads"
    
    url = f"https://www.youtube.com/watch?v={yt_link}"
    
    yt = YouTube(url, on_progress_callback=on_progress, 'WEB')
    print(yt.title)
    ys = yt.streams.get_audio_only()
    ys.download(output_path=LOCAL_PATH)
    
    file_name = f"{yt.title}.m4a"
    file_path = os.path.join(LOCAL_PATH, file_name)
    #import pdb; pdb.set_trace();
    #return FileResponse(path=file_path, filename=file_path, media_type='text/mp4')
    return FileResponse(file_path)

@app.get("/music/playlist/{yt_link}")
async def getMusicPlaylist(yt_link: str, start: int = 1, end: int = 5):
    return {"item_id": yt_link,"start": 1, "end": 5 }
