# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
u = urlparse(uri)
self.host = u.hostname
self.port = int(u.port or '21')
self.username = u.username
self.password = unquote(u.password or '')
self.path = u.path
self.use_active_mode = use_active_mode
self.overwrite = not feed_options or feed_options.get('overwrite', True)
