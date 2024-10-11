import argparse # pragma: no cover

parser = argparse.ArgumentParser() # pragma: no cover
type('Mock', (object,), {'SUPPRESS': argparse.SUPPRESS, 'add_argument': argparse.ArgumentParser.add_argument}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/view.py
from l3.Runtime import _l_
super().add_options(parser)
_l_(16479)
parser.add_argument('--headers', help=argparse.SUPPRESS)
_l_(16480)
