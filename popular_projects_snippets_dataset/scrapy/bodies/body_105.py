# Extracted from ./data/repos/scrapy/scrapy/shell.py
import scrapy

self.vars['scrapy'] = scrapy
self.vars['crawler'] = self.crawler
self.vars['item'] = self.item_class()
self.vars['settings'] = self.crawler.settings
self.vars['spider'] = spider
self.vars['request'] = request
self.vars['response'] = response
if self.inthread:
    self.vars['fetch'] = self.fetch
self.vars['view'] = open_in_browser
self.vars['shelp'] = self.print_help
self.update_vars(self.vars)
if not self.code:
    self.vars['banner'] = self.get_help()
