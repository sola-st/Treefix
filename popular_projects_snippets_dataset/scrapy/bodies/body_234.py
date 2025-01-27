# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
self.feed_options = feed_options
if feed_options is not None:
    self.item_classes = tuple(
        load_object(item_class) for item_class in feed_options.get("item_classes") or ()
    )
else:
    self.item_classes = tuple()
