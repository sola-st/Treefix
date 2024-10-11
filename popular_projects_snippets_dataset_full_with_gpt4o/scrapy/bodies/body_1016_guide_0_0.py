from typing import Union, AsyncIterable # pragma: no cover

response = type('MockResponse', (object,), {})() # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
result = type('MockIterable', (object,), {'__aiter__': lambda self: self, '__anext__': lambda self: (yield) })() # pragma: no cover
self = type('MockSelf', (object,), {'_evaluate_iterable': lambda self, resp, spi, res, init_val: result, '_process_spider_output': lambda self, resp, spi, res: result})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
recovered: Union[MutableChain, MutableAsyncChain]
_l_(21157)
if isinstance(result, AsyncIterable):
    _l_(21160)

    recovered = MutableAsyncChain()
    _l_(21158)
else:
    recovered = MutableChain()
    _l_(21159)
result = self._evaluate_iterable(response, spider, result, 0, recovered)
_l_(21161)
result = await maybe_deferred_to_future(self._process_spider_output(response, spider, result))
_l_(21162)
if isinstance(result, AsyncIterable):
    _l_(21164)

    aux = MutableAsyncChain(result, recovered)
    _l_(21163)
    exit(aux)
if isinstance(recovered, AsyncIterable):
    _l_(21167)

    recovered_collected = await collect_asyncgen(recovered)
    _l_(21165)
    recovered = MutableChain(recovered_collected)
    _l_(21166)
aux = MutableChain(result, recovered)  # type: ignore[arg-type]
_l_(21168)  # type: ignore[arg-type]
exit(aux)  # type: ignore[arg-type]
