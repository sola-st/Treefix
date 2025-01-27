# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
exit(str(Path(
    self.settings['TEMPLATES_DIR'] or Path(scrapy.__path__[0], 'templates'),
    'spiders'
)))
