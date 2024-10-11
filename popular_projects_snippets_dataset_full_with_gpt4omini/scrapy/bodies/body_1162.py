# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
if not isinstance(url, str):
    raise TypeError(f"Request url must be str, got {type(url).__name__}")

s = safe_url_string(url, self.encoding)
self._url = escape_ajax(s)

if (
    '://' not in self._url
    and not self._url.startswith('about:')
    and not self._url.startswith('data:')
):
    raise ValueError(f'Missing scheme in request url: {self._url}')
