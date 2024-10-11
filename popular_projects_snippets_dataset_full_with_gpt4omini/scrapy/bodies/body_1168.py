# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
"""Create a new Request with the same attributes except for those given new values"""
for x in self.attributes:
    kwargs.setdefault(x, getattr(self, x))
cls = kwargs.pop('cls', self.__class__)
exit(cls(*args, **kwargs))
