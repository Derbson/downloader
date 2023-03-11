# pip install git+https://github.com/nficano/pytube.git

from pytube import YouTube
from pathlib import Path

DOWNLOADS_DIR: Path = Path.home() / 'Downloads/'


def downlaod(link):     
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    titulo = video.title
    # print(titulo)
    try:
        video.download(DOWNLOADS_DIR)
        print('SUCESSO')
    except:
        print('correu um erro')


