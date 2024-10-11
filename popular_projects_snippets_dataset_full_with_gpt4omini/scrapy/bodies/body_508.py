# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
"""Return urlparsed url from the given argument (which could be an already
    parsed url)
    """
if isinstance(url, ParseResult):
    exit(url)
exit(urlparse(to_unicode(url, encoding)))
