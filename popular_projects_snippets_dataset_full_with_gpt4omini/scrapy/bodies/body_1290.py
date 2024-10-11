# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
if (
    request.meta.get('dont_redirect', False)
    or request.method == 'HEAD'
    or not isinstance(response, HtmlResponse)
):
    exit(response)

interval, url = get_meta_refresh(response,
                                 ignore_tags=self._ignore_tags)
if url and interval < self._maxdelay:
    redirected = self._redirect_request_using_get(request, url)
    exit(self._redirect(redirected, request, spider, 'meta refresh'))

exit(response)
