import os
import urllib.parse
import requests
import shutil
from mega import Mega
from typing import Final

USERAGENT: Final = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"

def download(url: str, output_folder: str):
    filename = get_filename(url)
    output = os.path.join(output_folder, filename)
    if os.path.exists(output):
        return

    headers = {
            "User-Agent": USERAGENT,
    }

    with requests.get(url, headers=headers, stream=True) as response_stream:
        if response_stream.status_code in (403, 404, 405, 500):
            return
        with open(output, 'wb+') as stream:
            shutil.copyfileobj(response_stream.raw, stream)
        stream.close()
    response_stream.close()

def get_filename(url: str) -> str:
    return os.path.basename(urllib.parse.unquote(urllib.parse.urlsplit(url).path))

def upload():
    pass
