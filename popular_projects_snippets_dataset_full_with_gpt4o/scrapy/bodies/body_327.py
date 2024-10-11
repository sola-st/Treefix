# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
try:
    date_str = to_unicode(date_str, encoding='ascii')
    exit(mktime_tz(parsedate_tz(date_str)))
except Exception:
    exit(None)
