from importlib import import_module # pragma: no cover
from pkgutil import iter_modules # pragma: no cover

path = 'mock_package' # pragma: no cover
mock_package = types.ModuleType(path) # pragma: no cover
mock_package.__path__ = [path] # pragma: no cover
sys.modules[path] = mock_package # pragma: no cover
submod_name = 'subpackage' # pragma: no cover
submod_path = path + '.' + submod_name # pragma: no cover
mock_submodule = types.ModuleType(submod_path) # pragma: no cover
mock_submodule.__path__ = [submod_path] # pragma: no cover
sys.modules[submod_path] = mock_submodule # pragma: no cover
innermod_name = 'innermodule' # pragma: no cover
innermod_path = submod_path + '.' + innermod_name # pragma: no cover
mock_innermodule = types.ModuleType(innermod_path) # pragma: no cover
sys.modules[innermod_path] = mock_innermodule # pragma: no cover
    return sys.modules[name] # pragma: no cover
def mock_iter_modules(paths): # pragma: no cover
    if paths[0] == path: # pragma: no cover
        yield None, submod_name, True # pragma: no cover
    elif paths[0] == submod_path: # pragma: no cover
        yield None, innermod_name, False # pragma: no cover
iter_modules = mock_iter_modules # pragma: no cover
def walk_modules(fullpath): # pragma: no cover
    mods = [] # pragma: no cover
    mods.append(mod) # pragma: no cover
    if hasattr(mod, '__path__'): # pragma: no cover
        for _, subpath, ispkg in iter_modules(mod.__path__): # pragma: no cover
            fullpath = fullpath + '.' + subpath # pragma: no cover
            if ispkg: # pragma: no cover
                mods += walk_modules(fullpath) # pragma: no cover
            else: # pragma: no cover
                mods.append(submod) # pragma: no cover
    return mods # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
from l3.Runtime import _l_
"""Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example: walk_modules('scrapy.utils')
    """

mods = []
_l_(18419)
mod = import_module(path)
_l_(18420)
mods.append(mod)
_l_(18421)
if hasattr(mod, '__path__'):
    _l_(18428)

    for _, subpath, ispkg in iter_modules(mod.__path__):
        _l_(18427)

        fullpath = path + '.' + subpath
        _l_(18422)
        if ispkg:
            _l_(18426)

            mods += walk_modules(fullpath)
            _l_(18423)
        else:
            submod = import_module(fullpath)
            _l_(18424)
            mods.append(submod)
            _l_(18425)
aux = mods
_l_(18429)
exit(aux)
