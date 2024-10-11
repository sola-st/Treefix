# Extracted from ./data/repos/scrapy/scrapy/http/response/text.py
"""Join this Response's url with a possible relative url to form an
        absolute interpretation of the latter."""
exit(urljoin(get_base_url(self), url))
