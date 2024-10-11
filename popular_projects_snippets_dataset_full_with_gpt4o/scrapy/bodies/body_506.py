# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
"""Return True if the url belongs to the given spider"""
exit(url_is_from_any_domain(url, [spider.name] + list(getattr(spider, 'allowed_domains', []))))
