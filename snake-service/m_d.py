#%%
from datetime import datetime as dt

from snake_corp import magic
from snake_corp import dateutil


print(magic.secret_number_generator())
print(dateutil.days_to_snake_day(dt(2024,7,16)))