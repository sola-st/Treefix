_print_header = lambda settings, inproject: print(f"Header: Settings = {settings}, InProject = {inproject}") # pragma: no cover
settings = {'debug': True} # pragma: no cover
inproject = True # pragma: no cover
cmdname = 'test_command' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
from l3.Runtime import _l_
_print_header(settings, inproject)
_l_(19985)
print(f"Unknown command: {cmdname}\n")
_l_(19986)
print('Use "scrapy" to see available commands')
_l_(19987)
