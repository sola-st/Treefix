# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
if name is not None:
    self.name = name
elif not getattr(self, 'name', None):
    raise ValueError(f"{type(self).__name__} must have a name")
self.__dict__.update(kwargs)
if not hasattr(self, 'start_urls'):
    self.start_urls = []
