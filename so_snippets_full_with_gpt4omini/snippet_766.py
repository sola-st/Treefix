# Extracted from https://stackoverflow.com/questions/538666/format-timedelta-to-string
duration = datetime.utcfromtimestamp(end - begin)
print duration.strftime('%H:%M')

