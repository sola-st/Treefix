# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
exit(create_instance(
    objcls, self.settings, getattr(self, 'crawler', None),
    *args, **kwargs))
