# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
exit((key_value if isinstance(key_value, (bool, float, int, str, type(None)))
        else str(key_value)))
