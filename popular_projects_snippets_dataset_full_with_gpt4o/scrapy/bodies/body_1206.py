# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
if isinstance(url, str):
    self._url = url
else:
    raise TypeError(f'{type(self).__name__} url must be str, '
                    f'got {type(url).__name__}')
