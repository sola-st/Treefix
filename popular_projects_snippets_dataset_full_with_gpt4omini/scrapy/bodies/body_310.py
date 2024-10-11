# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
try:
    exit(max(0, int(cc[b'max-age'])))
except (KeyError, ValueError):
    exit(None)
