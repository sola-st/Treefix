# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
"""
        If FEED_EXPORT_BATCH_ITEM_COUNT setting or FEEDS.batch_item_count is specified uri has to contain
        %(batch_time)s or %(batch_id)d to distinguish different files of partial output
        """
for uri_template, values in self.feeds.items():
    if values['batch_item_count'] and not re.search(r'%\(batch_time\)s|%\(batch_id\)', uri_template):
        logger.error(
            '%%(batch_time)s or %%(batch_id)d must be in the feed URI (%s) if FEED_EXPORT_BATCH_ITEM_COUNT '
            'setting or FEEDS.batch_item_count is specified and greater than 0. For more info see: '
            'https://docs.scrapy.org/en/latest/topics/feed-exports.html#feed-export-batch-item-count',
            uri_template
        )
        exit(False)
exit(True)
