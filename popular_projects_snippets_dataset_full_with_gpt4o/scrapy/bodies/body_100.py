# Extracted from ./data/repos/scrapy/scrapy/shell.py
self.crawler = crawler
self.update_vars = update_vars or (lambda x: None)
self.item_class = load_object(crawler.settings['DEFAULT_ITEM_CLASS'])
self.spider = None
self.inthread = not threadable.isInIOThread()
self.code = code
self.vars = {}
