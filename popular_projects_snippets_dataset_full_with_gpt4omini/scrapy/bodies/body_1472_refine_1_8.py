from typing import List, Optional, Callable # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    def _filter(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
response = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
result = [{'data': 'result1'}, {'data': 'result2'}, {'data': 'result3'}] # pragma: no cover

from typing import List, Dict, Any, Callable, AsyncIterable # pragma: no cover
import asyncio # pragma: no cover

class Mock:# pragma: no cover
    def _init_depth(self, response, spider):# pragma: no cover
        pass# pragma: no cover
    def _filter(self, r, response, spider):# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
response: Dict[str, Any] = {'url': 'http://example.com', 'status': 200} # pragma: no cover
spider: Dict[str, Any] = {'name': 'example_spider'} # pragma: no cover
async def generate_results() -> AsyncIterable[Dict[str, Any]]:# pragma: no cover
    for i in range(1, 4):# pragma: no cover
        yield {'data': f'result{i}'}# pragma: no cover
# pragma: no cover
result: AsyncIterable[Dict[str, Any]] = generate_results() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
from l3.Runtime import _l_
self._init_depth(response, spider)
_l_(8646)
async for r in result or ():
    _l_(8649)

    if self._filter(r, response, spider):
        _l_(8648)

        aux = r
        _l_(8647)
        exit(aux)
