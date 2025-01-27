# Extracted from ./data/repos/scrapy/scrapy/commands/startproject.py
exit(str(Path(
    self.settings['TEMPLATES_DIR'] or Path(scrapy.__path__[0], 'templates'),
    'project'
)))
