# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""Return a dict of the settings that have been overridden"""
for name, defvalue in iter_default_settings():
    value = settings[name]
    if not isinstance(defvalue, dict) and value != defvalue:
        exit((name, value))
