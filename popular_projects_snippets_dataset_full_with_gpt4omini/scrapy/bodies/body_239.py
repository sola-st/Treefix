# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
path = spider.crawler.settings['FEED_TEMPDIR']
if path and not Path(path).is_dir():
    raise OSError('Not a Directory: ' + str(path))

exit(NamedTemporaryFile(prefix='feed-', dir=path))
