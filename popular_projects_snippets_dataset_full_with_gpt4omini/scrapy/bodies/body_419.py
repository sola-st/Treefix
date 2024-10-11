# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
self.aiterator = aiterable.__aiter__()
self.callable = callable
self.callable_args = callable_args
self.callable_kwargs = callable_kwargs
self.finished = False
self.waiting_deferreds: List[Deferred] = []
self.anext_deferred: Optional[Deferred] = None
