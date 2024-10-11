# Extracted from ./data/repos/scrapy/scrapy/exporters.py
self.item_element = kwargs.pop('item_element', 'item')
self.root_element = kwargs.pop('root_element', 'items')
super().__init__(**kwargs)
if not self.encoding:
    self.encoding = 'utf-8'
self.xg = XMLGenerator(file, encoding=self.encoding)
