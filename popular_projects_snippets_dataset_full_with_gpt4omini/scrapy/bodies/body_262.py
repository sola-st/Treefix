# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
for uri, feed_options in self.feeds.items():
    uri_params = self._get_uri_params(spider, feed_options['uri_params'])
    self.slots.append(self._start_new_batch(
        batch_id=1,
        uri=uri % uri_params,
        feed_options=feed_options,
        spider=spider,
        uri_template=uri,
    ))
