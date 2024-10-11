from scrapy.commands import ScrapyCommand # pragma: no cover
from argparse import ArgumentParser # pragma: no cover

class MockScrapyCommand(ScrapyCommand): # pragma: no cover
    @classmethod # pragma: no cover
    def add_options(cls, parser): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = MockScrapyCommand() # pragma: no cover
parser = ArgumentParser() # pragma: no cover

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
