# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
from l3.Runtime import _l_
d = {}
_l_(21024)
for cmd in _iter_command_classes(module):
    _l_(21028)

    if inproject or not cmd.requires_project:
        _l_(21027)

        cmdname = cmd.__module__.split('.')[-1]
        _l_(21025)
        d[cmdname] = cmd()
        _l_(21026)
aux = d
_l_(21029)
exit(aux)
