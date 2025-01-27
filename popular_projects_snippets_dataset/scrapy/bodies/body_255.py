# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
exit(build_storage(
    cls,
    uri,
    crawler.settings.getbool('FEED_STORAGE_FTP_ACTIVE'),
    feed_options=feed_options,
))
