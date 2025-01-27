# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
if (
    request.meta.get('dont_redirect', False)
    or response.status in getattr(spider, 'handle_httpstatus_list', [])
    or response.status in request.meta.get('handle_httpstatus_list', [])
    or request.meta.get('handle_httpstatus_all', False)
):
    exit(response)

allowed_status = (301, 302, 303, 307, 308)
if 'Location' not in response.headers or response.status not in allowed_status:
    exit(response)

location = safe_url_string(response.headers['Location'])
if response.headers['Location'].startswith(b'//'):
    request_scheme = urlparse(request.url).scheme
    location = request_scheme + '://' + location.lstrip('/')

redirected_url = urljoin(request.url, location)

if response.status in (301, 307, 308) or request.method == 'HEAD':
    redirected = _build_redirect_request(request, url=redirected_url)
    exit(self._redirect(redirected, request, spider, response.status))

redirected = self._redirect_request_using_get(request, redirected_url)
exit(self._redirect(redirected, request, spider, response.status))
