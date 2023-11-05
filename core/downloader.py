from urllib.request import urlopen

import requests
from PySide6.QtCore import QThread, Signal

class Downloader(QThread):

    # Signal for the window to establish the maximum value
    # of the progress bar.
    setTotalProgress = Signal(int)
    # Signal to increase the progress.
    setCurrentProgress = Signal(int)
    # Signal to be emitted when the file has been downloaded successfully.
    succeeded = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        download_url = "https://fastupload.io/MJxqhzM1wZIgA6x/download/create"
        with requests.post(download_url) as response:
            r = response
        print(r.status_code)
        url = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/618503555/a18e1ea8-318b-4896-8edc-fc9d31f42ce4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231105T132407Z&X-Amz-Expires=300&X-Amz-Signature=9564673ce6c5a7bddffa5841b9ef8526236522f215afafc78e55eba7967f556d&X-Amz-SignedHeaders=host&actor_id=49392440&key_id=0&repo_id=618503555&response-content-disposition=attachment%3B%20filename%3DSD-Prompt-Reader-1.3.4-Windows-x64-v2.zip&response-content-type=application%2Foctet-stream"
        filename = "tmp.zip"
        readBytes = 0
        chunkSize = 2048
        # Open the URL address.
        with urlopen(url) as r:
            # Tell the window the amount of bytes to be downloaded.
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(filename, "ab") as f:
                while True:
                    # Read a piece of the file we are downloading.
                    chunk = r.read(chunkSize)
                    # If the result is `None`, that means data is not
                    # downloaded yet. Just keep waiting.
                    if chunk is None:
                        continue
                    # If the result is an empty `bytes` instance, then
                    # the file is complete.
                    elif chunk == b"":
                        break
                    # Write into the local file the downloaded chunk.
                    f.write(chunk)
                    readBytes += chunkSize
                    # Tell the window how many bytes we have received.
                    self.setCurrentProgress.emit(readBytes)
        # If this line is reached then no exception has ocurred in
        # the previous lines.
        self.succeeded.emit()