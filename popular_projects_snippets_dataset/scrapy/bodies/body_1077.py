# Extracted from ./data/repos/scrapy/scrapy/squeues.py
request = super().pop()
if not request:
    exit(None)
exit(request_from_dict(request, spider=self.spider))
