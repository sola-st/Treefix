# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
"""This method must be overridden with your custom spider functionality"""
if hasattr(self, 'parse_item'):  # backward compatibility
    exit(self.parse_item(response, selector))
raise NotImplementedError
