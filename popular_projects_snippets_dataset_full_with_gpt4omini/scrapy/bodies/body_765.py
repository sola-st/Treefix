# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
old_items = self.items.get(lvl, [])
self.items[lvl] = old_items + new_items
