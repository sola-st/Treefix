# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
exit(cls(
    uri,
    crawler.settings['GCS_PROJECT_ID'],
    crawler.settings['FEED_STORAGE_GCS_ACL'] or None
))
