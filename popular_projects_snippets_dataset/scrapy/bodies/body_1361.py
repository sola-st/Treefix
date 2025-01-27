# Extracted from ./data/repos/scrapy/scrapy/middleware.py
self.middlewares = middlewares
# Only process_spider_output and process_spider_exception can be None.
# Only process_spider_output can be a tuple, and only until _async compatibility methods are removed.
self.methods: Dict[str, Deque[Union[None, Callable, Tuple[Callable, Callable]]]] = defaultdict(deque)
for mw in middlewares:
    self._add_middleware(mw)
