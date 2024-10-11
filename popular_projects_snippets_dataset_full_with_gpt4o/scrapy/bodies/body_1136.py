# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
exit([to_unicode(v, errors='replace')
        for v in self.response.headers.getlist(name)])
