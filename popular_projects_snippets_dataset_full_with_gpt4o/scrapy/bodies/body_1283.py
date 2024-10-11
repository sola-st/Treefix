# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
redirect_request = source_request.replace(
    url=url,
    **kwargs,
    cookies=None,
)
if 'Cookie' in redirect_request.headers:
    source_request_netloc = urlparse_cached(source_request).netloc
    redirect_request_netloc = urlparse_cached(redirect_request).netloc
    if source_request_netloc != redirect_request_netloc:
        del redirect_request.headers['Cookie']
exit(redirect_request)
