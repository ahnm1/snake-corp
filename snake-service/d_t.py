#%%
from pprint import pprint
from pathlib import Path

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
# from snake_corp import downloader

# r = downloader.DownloadUrl(
#     urls         = urls,
#     target_path  = target_path,
#     thread_count = 4
# ).download()

#%% - Timestamp Generator

from snake_corp import TimestampGenerator as tg

year, month, days = tg.TimestampGenerator(2023,2).get_days_for_month()
year, month, days
#%%
timestamps_month = (
    tg.TimestampGenerator(year,month)
    .get_timestamps(days, dt_pattern='%Y-%m-%d %H:%M:%S')
)
pprint(timestamps_month)
#%%
len(days)