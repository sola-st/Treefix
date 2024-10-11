import types # pragma: no cover

_iter_command_classes = lambda module: [type('Mock', (object,), {'__module__': module, 'requires_project': False, '__call__': lambda self: 'dummy_command'})] # pragma: no cover
module = 'dummy_module' # pragma: no cover
inproject = True # pragma: no cover

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
