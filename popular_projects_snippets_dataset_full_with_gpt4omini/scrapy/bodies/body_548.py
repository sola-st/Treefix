# Extracted from ./data/repos/scrapy/scrapy/utils/spider.py
"""Return an iterator over all spider classes defined in the given module
    that can be instantiated (i.e. which have name)
    """
# this needs to be imported here until get rid of the spider manager
# singleton in scrapy.spider.spiders
from scrapy.spiders import Spider

for obj in vars(module).values():
    if (
        inspect.isclass(obj)
        and issubclass(obj, Spider)
        and obj.__module__ == module.__name__
        and getattr(obj, 'name', None)
    ):
        exit(obj)
