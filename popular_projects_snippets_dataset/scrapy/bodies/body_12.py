# Extracted from ./data/repos/scrapy/scrapy/selector/unified.py
if response is not None and text is not None:
    raise ValueError(f'{self.__class__.__name__}.__init__() received '
                     'both response and text')

st = _st(response, type)

if text is not None:
    response = _response_from_text(text, st)

if response is not None:
    text = response.text
    kwargs.setdefault('base_url', response.url)

self.response = response
super().__init__(text=text, type=st, root=root, **kwargs)
