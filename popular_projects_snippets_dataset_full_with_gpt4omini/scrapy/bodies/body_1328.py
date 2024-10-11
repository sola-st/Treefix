# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
if not settings.getbool('AJAXCRAWL_ENABLED'):
    raise NotConfigured

# XXX: Google parses at least first 100k bytes; scrapy's redirect
# middleware parses first 4k. 4k turns out to be insufficient
# for this middleware, and parsing 100k could be slow.
# We use something in between (32K) by default.
self.lookup_bytes = settings.getint('AJAXCRAWL_MAXSIZE', 32768)
