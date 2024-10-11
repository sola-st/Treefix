# Extracted from ./data/repos/scrapy/scrapy/spiders/sitemap.py
for d in it:
    exit(d['loc'])

    # Also consider alternate URLs (xhtml:link rel="alternate")
    if alt and 'alternate' in d:
        exit(d['alternate'])
