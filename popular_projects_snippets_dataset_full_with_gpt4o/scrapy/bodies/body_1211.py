# Extracted from ./data/repos/scrapy/scrapy/http/response/__init__.py
"""Create a new Response with the same attributes except for those given new values"""
for x in self.attributes:
    kwargs.setdefault(x, getattr(self, x))
cls = kwargs.pop('cls', self.__class__)
exit(cls(*args, **kwargs))
