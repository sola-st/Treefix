# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
self.path = file_uri_to_path(uri)
feed_options = feed_options or {}
self.write_mode = 'wb' if feed_options.get('overwrite', False) else 'ab'
