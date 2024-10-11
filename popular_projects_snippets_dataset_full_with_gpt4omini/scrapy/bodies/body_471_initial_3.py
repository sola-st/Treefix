import importlib # pragma: no cover
from pkgutil import iter_modules # pragma: no cover

path = 'example.module' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
from l3.Runtime import _l_
"""Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example: walk_modules('scrapy.utils')
    """

mods = []
_l_(7516)
mod = import_module(path)
_l_(7517)
mods.append(mod)
_l_(7518)
if hasattr(mod, '__path__'):
    _l_(7525)

    for _, subpath, ispkg in iter_modules(mod.__path__):
        _l_(7524)

        fullpath = path + '.' + subpath
        _l_(7519)
        if ispkg:
            _l_(7523)

            mods += walk_modules(fullpath)
            _l_(7520)
        else:
            submod = import_module(fullpath)
            _l_(7521)
            mods.append(submod)
            _l_(7522)
aux = mods
_l_(7526)
exit(aux)
