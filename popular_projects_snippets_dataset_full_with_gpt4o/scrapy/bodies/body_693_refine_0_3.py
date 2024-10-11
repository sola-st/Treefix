import argparse # pragma: no cover
import sys # pragma: no cover

parser = argparse.ArgumentParser() # pragma: no cover
argparse.SUPPRESS = '==SUPPRESS== ' # pragma: no cover

import argparse # pragma: no cover

class BaseParser: # pragma: no cover
    def add_options(self, parser): # pragma: no cover
        parser.add_argument('--verbose', action='store_true', help='increase output verbosity') # pragma: no cover
 # pragma: no cover
class CustomParser(BaseParser): # pragma: no cover
    def add_options(self, parser): # pragma: no cover
        super().add_options(parser) # pragma: no cover
 # pragma: no cover
parser = argparse.ArgumentParser() # pragma: no cover
argparse.SUPPRESS = '==SUPPRESS== ' # pragma: no cover
custom_parser = CustomParser() # pragma: no cover
custom_parser.add_options(parser) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/view.py
from l3.Runtime import _l_
super().add_options(parser)
_l_(16479)
parser.add_argument('--headers', help=argparse.SUPPRESS)
_l_(16480)
