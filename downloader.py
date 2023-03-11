# pip install git+https://github.com/nficano/pytube.git

from pytube import YouTube
from pytube.cli import on_progress
from pathlib import Path
from pytube.exceptions import PytubeError, RegexMatchError
import re

DOWNLOADS_DIR: Path = Path.home() / 'Downloads/'


def downlaod(link):
    if link and validator_url(link):
        video = YouTube(link ,on_progress_callback=on_progress)
        video = video.streams.get_highest_resolution()
        # titulo = video.title
        
        try:
            print(f'Download...%')
            video.download(DOWNLOADS_DIR)
            print('\nCompleted')
        except:
            print('adicione uma url válida')
            
def validator_url(url):
    pattern = 'youtube'
    if re.search(f'(https://www.){pattern}(.com)', url):
        return True
    return False