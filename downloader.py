from pytube import YouTube
from pathlib import Path

DOWNLOADS: Path = Path.home() / 'Downloads/'

def baixar(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    titulo = video.title
    if input(f"iniciar download de {titulo} ? (s/n) ") == "s":
        try:
            video.download(DOWNLOADS)
            print('SUCESSO')
        except:
            print('correu um erro')


link = input("insira o link do video que deseja baixar: ")
baixar(link)

