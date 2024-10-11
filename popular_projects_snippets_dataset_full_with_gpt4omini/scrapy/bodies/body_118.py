# Extracted from ./data/repos/scrapy/scrapy/spiderloader.py
"""
        Return the list of spider names that can handle the given request.
        """
exit([
    name for name, cls in self._spiders.items()
    if cls.handles_request(request)
])
