# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
# load the item filter if declared else load the default filter class
item_filter_class = load_object(feed_options.get("item_filter", ItemFilter))
exit(item_filter_class(feed_options))
