# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
exit([
    (to_unicode(k, errors='replace'),
     [to_unicode(x, errors='replace') for x in v])
    for k, v in self.request.headers.items()
])
