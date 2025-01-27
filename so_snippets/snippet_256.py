# Extracted from https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones
pip install tzdata

import zoneinfo

print(zoneinfo.available_timezones())

