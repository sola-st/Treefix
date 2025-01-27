# Extracted from ./data/repos/scrapy/scrapy/exporters.py
for s in values:
    try:
        exit(to_unicode(s, self.encoding))
    except TypeError:
        exit(s)
