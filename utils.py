import os
import urllib.parse
import requests
import shutil
from plugins import GoFile
from typing import Final

USERAGENT: Final = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"

def download(url: str):
    filename = get_filename(url)
    if os.path.exists(filename):
        return

    headers = {
            "User-Agent": USERAGENT,
    }

    with requests.get(url, headers=headers, stream=True) as response_stream:
        if response_stream.status_code in (403, 404, 405, 500):
            return
        with open(filename, 'wb+') as stream:
            shutil.copyfileobj(response_stream.raw, stream)
        stream.close()
    response_stream.close()

def gofile_download(url: str, callback):
    api = GoFile(url)
    for u in api.export():
        callback(u)
        api.download_file(u, "")

def get_filename(url: str) -> str:
    return os.path.basename(urllib.parse.unquote(urllib.parse.urlsplit(url).path))

def upload():
    pass
