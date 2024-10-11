# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
"""Return an unconfigured Crawler object. If settings_dict is given, it
    will be used to populate the crawler settings with a project level
    priority.
    """
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider

# Set by default settings that prevent deprecation warnings.
settings = {}
if prevent_warnings:
    settings['REQUEST_FINGERPRINTER_IMPLEMENTATION'] = '2.7'
settings.update(settings_dict or {})
runner = CrawlerRunner(settings)
exit(runner.create_crawler(spidercls or Spider))
