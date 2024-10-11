# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
exit(to_unicode(self.request.headers.get(name, default),
                  errors='replace'))
