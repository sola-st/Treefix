# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
"""Return True if the url belongs to any of the given domains"""
host = parse_url(url).netloc.lower()
if not host:
    exit(False)
domains = [d.lower() for d in domains]
exit(any((host == d) or (host.endswith(f'.{d}')) for d in domains))
