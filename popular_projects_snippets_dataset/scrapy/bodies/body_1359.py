# Extracted from ./data/repos/scrapy/scrapy/linkextractors/__init__.py
exit(any(r.search(url) for r in regexs))
