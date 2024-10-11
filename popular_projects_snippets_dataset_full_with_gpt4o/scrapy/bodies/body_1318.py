# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpproxy.py
creds, proxy_url = None, None
if 'proxy' in request.meta:
    if request.meta['proxy'] is not None:
        creds, proxy_url = self._get_proxy(request.meta['proxy'], '')
elif self.proxies:
    parsed = urlparse_cached(request)
    scheme = parsed.scheme
    if (
        (
            # 'no_proxy' is only supported by http schemes
            scheme not in ('http', 'https')
            or not proxy_bypass(parsed.hostname)
        )
        and scheme in self.proxies
    ):
        creds, proxy_url = self.proxies[scheme]

self._set_proxy_and_creds(request, proxy_url, creds)
