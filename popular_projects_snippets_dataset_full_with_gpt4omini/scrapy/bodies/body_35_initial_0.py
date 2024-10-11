_iter_command_classes = lambda module: [type('CommandA', (), {'requires_project': False, '__module__': 'commands.ModuleA'}), type('CommandB', (), {'requires_project': True, '__module__': 'commands.ModuleB'})] # pragma: no cover
module = 'commands.ModuleA' # pragma: no cover
inproject = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
from l3.Runtime import _l_
d = {}
_l_(9594)
for cmd in _iter_command_classes(module):
    _l_(9598)

    if inproject or not cmd.requires_project:
        _l_(9597)

        cmdname = cmd.__module__.split('.')[-1]
        _l_(9595)
        d[cmdname] = cmd()
        _l_(9596)
aux = d
_l_(9599)
exit(aux)
