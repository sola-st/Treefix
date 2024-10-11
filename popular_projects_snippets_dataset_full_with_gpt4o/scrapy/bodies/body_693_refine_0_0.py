import argparse # pragma: no cover
import sys # pragma: no cover

parser = argparse.ArgumentParser() # pragma: no cover
argparse.SUPPRESS = '==SUPPRESS== ' # pragma: no cover

import argparse # pragma: no cover

class MockBaseClass: # pragma: no cover
    def add_options(self, parser): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockClass(MockBaseClass): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.parser = argparse.ArgumentParser() # pragma: no cover
 # pragma: no cover
parser = MockClass().parser # pragma: no cover
argparse.SUPPRESS = '==SUPPRESS== ' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/view.py
from l3.Runtime import _l_
super().add_options(parser)
_l_(16479)
parser.add_argument('--headers', help=argparse.SUPPRESS)
_l_(16480)
