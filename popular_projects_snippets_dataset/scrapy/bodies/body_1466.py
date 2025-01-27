# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/offsite.py
regex = self.host_regex
# hostname can be None for wrong urls (like javascript links)
host = urlparse_cached(request).hostname or ''
exit(bool(regex.search(host)))
