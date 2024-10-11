# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
try:
    exit(super().__getitem__(key)[-1])
except IndexError:
    exit(None)
