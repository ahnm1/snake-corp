#%%
from pathlib import Path
from datetime import datetime as dt

from snake_corp import dateutil
from snake_corp import magic
from snake_corp import downloader

print(magic.secret_number_generator())
print(dateutil.days_to_snake_day(dt(2024,7,16)))

#%%
urls = [
    'http://data.gdeltproject.org/gdeltv2/20230925081500.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925080000.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925074500.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925073000.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925071500.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925070000.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925064500.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925063000.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925061500.gkg.csv.zip',
    'http://data.gdeltproject.org/gdeltv2/20230925060000.gkg.csv.zip'
]
target_path = Path('./downloads/')
target_path

#%% Does not work in interactive window
r = downloader.DownloadUrl(
    urls         = urls,
    target_path  = target_path,
    thread_count = 4
).download()

#%%
r