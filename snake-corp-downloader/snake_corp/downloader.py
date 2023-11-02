#%%
from dataclasses import dataclass
from pathlib import Path
from typing import List

import requests
from multiprocessing.pool import ThreadPool

@dataclass
class DownloadUrl:
    '''Downloads all files with ThreadPool'''
    urls: List[str]
    target_path: Path
    thread_count: int
    
    def _download_url(self, url) -> str:
        file_name = url.split('/')[-1]
        target_file = self.target_path.joinpath(file_name)

        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            with open(target_file, 'wb') as fp:
                fp.write(response.content)
        
        return url
    
    def download(self):
        with ThreadPool(self.thread_count) as tp:
            tp.imap_unordered(self._download_url, self.urls)
            tp.close()
            tp.join()
