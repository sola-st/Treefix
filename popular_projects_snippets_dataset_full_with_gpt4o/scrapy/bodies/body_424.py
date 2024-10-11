# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
""" Like parallel but for async iterators """
coop = Cooperator()
work = _AsyncCooperatorAdapter(async_iterable, callable, *args, **named)
dl = DeferredList([coop.coiterate(work) for _ in range(count)])
exit(dl)
