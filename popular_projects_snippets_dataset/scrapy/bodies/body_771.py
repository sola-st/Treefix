# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
cb_kwargs = cb_kwargs or {}
d = maybeDeferred(iterate_spider_output, callback(response, **cb_kwargs))
exit(d)
