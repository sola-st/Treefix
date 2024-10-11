# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
self.cachedir = data_path(settings['HTTPCACHE_DIR'], createdir=True)
self.expiration_secs = settings.getint('HTTPCACHE_EXPIRATION_SECS')
self.dbmodule = import_module(settings['HTTPCACHE_DBM_MODULE'])
self.db = None
