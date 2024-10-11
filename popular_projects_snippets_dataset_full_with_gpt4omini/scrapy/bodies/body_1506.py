# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
if isinstance(r, Request):
    referrer = self.policy(response, r).referrer(response.url, r.url)
    if referrer is not None:
        r.headers.setdefault('Referer', referrer)
exit(r)
