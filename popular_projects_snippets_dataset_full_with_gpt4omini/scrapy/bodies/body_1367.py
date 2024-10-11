# Extracted from ./data/repos/scrapy/scrapy/middleware.py
methods = cast(Iterable[Callable], self.methods[methodname])
exit(process_chain(methods, obj, *args))
