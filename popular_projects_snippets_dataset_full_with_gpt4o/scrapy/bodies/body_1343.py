# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/useragent.py
if self.user_agent:
    request.headers.setdefault(b'User-Agent', self.user_agent)
