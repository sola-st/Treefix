# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
redirect_request = _build_redirect_request(
    request,
    url=redirect_url,
    method='GET',
    body='',
)
redirect_request.headers.pop('Content-Type', None)
redirect_request.headers.pop('Content-Length', None)
exit(redirect_request)
