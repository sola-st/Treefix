# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
super().__init__(settings)
self._ignore_tags = settings.getlist('METAREFRESH_IGNORE_TAGS')
self._maxdelay = settings.getint('METAREFRESH_MAXDELAY')
