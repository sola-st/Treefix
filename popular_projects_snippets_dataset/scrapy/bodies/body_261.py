# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
self.crawler = crawler
self.settings = crawler.settings
self.feeds = {}
self.slots = []
self.filters = {}

if not self.settings['FEEDS'] and not self.settings['FEED_URI']:
    raise NotConfigured

# Begin: Backward compatibility for FEED_URI and FEED_FORMAT settings
if self.settings['FEED_URI']:
    warnings.warn(
        'The `FEED_URI` and `FEED_FORMAT` settings have been deprecated in favor of '
        'the `FEEDS` setting. Please see the `FEEDS` setting docs for more details',
        category=ScrapyDeprecationWarning, stacklevel=2,
    )
    uri = str(self.settings['FEED_URI'])  # handle pathlib.Path objects
    feed_options = {'format': self.settings.get('FEED_FORMAT', 'jsonlines')}
    self.feeds[uri] = feed_complete_default_values_from_settings(feed_options, self.settings)
    self.filters[uri] = self._load_filter(feed_options)
# End: Backward compatibility for FEED_URI and FEED_FORMAT settings

# 'FEEDS' setting takes precedence over 'FEED_URI'
for uri, feed_options in self.settings.getdict('FEEDS').items():
    uri = str(uri)  # handle pathlib.Path objects
    self.feeds[uri] = feed_complete_default_values_from_settings(feed_options, self.settings)
    self.filters[uri] = self._load_filter(feed_options)

self.storages = self._load_components('FEED_STORAGES')
self.exporters = self._load_components('FEED_EXPORTERS')
for uri, feed_options in self.feeds.items():
    if not self._storage_supported(uri, feed_options):
        raise NotConfigured
    if not self._settings_are_valid():
        raise NotConfigured
    if not self._exporter_supported(feed_options['format']):
        raise NotConfigured
