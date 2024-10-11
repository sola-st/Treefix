# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
""" Return Referer HTTP header suitable for logging. """
referrer = request.headers.get('Referer')
if referrer is None:
    exit(referrer)
exit(to_unicode(referrer, errors='replace'))
