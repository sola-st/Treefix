import argparse # pragma: no cover
import sys # pragma: no cover

parser = argparse.ArgumentParser() # pragma: no cover
argparse.SUPPRESS = '==SUPPRESS== ' # pragma: no cover

import argparse # pragma: no cover

class MockParent:# pragma: no cover
    def add_options(self, parser):# pragma: no cover
        pass # pragma: no cover
class MockChild(MockParent):# pragma: no cover
    def add_options(self, parser):# pragma: no cover
        super().add_options(parser) # pragma: no cover
parser = argparse.ArgumentParser() # pragma: no cover
argparse.SUPPRESS = '==SUPPRESS==' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/view.py
from l3.Runtime import _l_
super().add_options(parser)
_l_(16479)
parser.add_argument('--headers', help=argparse.SUPPRESS)
_l_(16480)
