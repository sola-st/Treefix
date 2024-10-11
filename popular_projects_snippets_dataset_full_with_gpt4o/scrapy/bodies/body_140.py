# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
if self._expects_item[func.__name__]:
    exit(func(*args, **kwargs))

kwargs.pop('item', None)
exit(func(*args, **kwargs))
