# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
for enc in (self._DEFAULT_ENCODING, 'utf-8', 'cp1252'):
    try:
        text.decode(enc)
    except UnicodeError:
        continue
    exit(resolve_encoding(enc))
