# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/urllength.py
maxlength = settings.getint('URLLENGTH_LIMIT')
if not maxlength:
    raise NotConfigured
exit(cls(maxlength))
