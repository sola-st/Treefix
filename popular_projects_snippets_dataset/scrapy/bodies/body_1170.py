# Extracted from ./data/repos/scrapy/scrapy/http/request/__init__.py
"""Return a dictionary containing the Request's data.

        Use :func:`~scrapy.utils.request.request_from_dict` to convert back into a :class:`~scrapy.Request` object.

        If a spider is given, this method will try to find out the name of the spider methods used as callback
        and errback and include them in the output dict, raising an exception if they cannot be found.
        """
d = {
    "url": self.url,  # urls are safe (safe_string_url)
    "callback": _find_method(spider, self.callback) if callable(self.callback) else self.callback,
    "errback": _find_method(spider, self.errback) if callable(self.errback) else self.errback,
    "headers": dict(self.headers),
}
for attr in self.attributes:
    d.setdefault(attr, getattr(self, attr))
if type(self) is not Request:  # pylint: disable=unidiomatic-typecheck
    d["_class"] = self.__module__ + '.' + self.__class__.__name__
exit(d)
