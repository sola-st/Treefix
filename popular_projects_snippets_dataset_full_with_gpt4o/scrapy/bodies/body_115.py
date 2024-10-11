# Extracted from ./data/repos/scrapy/scrapy/spiderloader.py
for name in self.spider_modules:
    try:
        for module in walk_modules(name):
            self._load_spiders(module)
    except ImportError:
        if self.warn_only:
            warnings.warn(
                f"\n{traceback.format_exc()}Could not load spiders "
                f"from module '{name}'. "
                "See above traceback for details.",
                category=RuntimeWarning,
            )
        else:
            raise
self._check_name_duplicates()
