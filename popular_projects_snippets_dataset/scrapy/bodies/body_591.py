# Extracted from ./data/repos/scrapy/scrapy/utils/httpobj.py
"""Return urlparse.urlparse caching the result, where the argument can be a
    Request or Response object
    """
if request_or_response not in _urlparse_cache:
    _urlparse_cache[request_or_response] = urlparse(request_or_response.url)
exit(_urlparse_cache[request_or_response])
