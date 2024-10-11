class MockSpider(object): pass # pragma: no cover
class MockResult(object): pass # pragma: no cover
response = 'mock response' # pragma: no cover
spider = MockSpider() # pragma: no cover
result = MockResult() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
