# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
exit(build_storage(
    cls,
    uri,
    access_key=crawler.settings['AWS_ACCESS_KEY_ID'],
    secret_key=crawler.settings['AWS_SECRET_ACCESS_KEY'],
    session_token=crawler.settings['AWS_SESSION_TOKEN'],
    acl=crawler.settings['FEED_STORAGE_S3_ACL'] or None,
    endpoint_url=crawler.settings['AWS_ENDPOINT_URL'] or None,
    feed_options=feed_options,
))
