import argparse # pragma: no cover

parser = argparse.ArgumentParser() # pragma: no cover
argparse = type('Mock', (object,), {'SUPPRESS': object()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/view.py
from l3.Runtime import _l_
super().add_options(parser)
_l_(5439)
parser.add_argument('--headers', help=argparse.SUPPRESS)
_l_(5440)
