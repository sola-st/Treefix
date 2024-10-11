# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
exit({self._get_key(k): (v._to_dict() if isinstance(v, BaseSettings) else v)
        for k, v in self.items()})
