from scrapy.commands import ScrapyCommand # pragma: no cover
import argparse # pragma: no cover

class MockScrapyCommand(ScrapyCommand): pass # pragma: no cover
self = MockScrapyCommand() # pragma: no cover
parser = argparse.ArgumentParser() # pragma: no cover

from scrapy.commands import ScrapyCommand # pragma: no cover
import argparse # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

class MockScrapyCommand(ScrapyCommand): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = Settings({'LOG_LEVEL': 'INFO'}) # pragma: no cover
self = MockScrapyCommand() # pragma: no cover
parser = argparse.ArgumentParser() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/__init__.py
from l3.Runtime import _l_
ScrapyCommand.add_options(self, parser)
_l_(5157)
parser.add_argument("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                    help="set spider argument (may be repeated)")
_l_(5158)
parser.add_argument("-o", "--output", metavar="FILE", action="append",
                    help="append scraped items to the end of FILE (use - for stdout),"
                         " to define format set a colon at the end of the output URI (i.e. -o FILE:FORMAT)")
_l_(5159)
parser.add_argument("-O", "--overwrite-output", metavar="FILE", action="append",
                    help="dump scraped items into FILE, overwriting any existing file,"
                         " to define format set a colon at the end of the output URI (i.e. -O FILE:FORMAT)")
_l_(5160)
parser.add_argument("-t", "--output-format", metavar="FORMAT",
                    help="format to use for dumping items")
_l_(5161)
