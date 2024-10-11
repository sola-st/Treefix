from importlib import import_module # pragma: no cover
from pkgutil import iter_modules # pragma: no cover

path = 'mock_package' # pragma: no cover
mock_package = types.ModuleType(path) # pragma: no cover
mock_package.__path__ = [path] # pragma: no cover
sys.modules[path] = mock_package # pragma: no cover
subpkg_name = 'subpkg' # pragma: no cover
subpkg_path = f'{path}.{subpkg_name}' # pragma: no cover
mock_subpkg = types.ModuleType(subpkg_path) # pragma: no cover
mock_subpkg.__path__ = [subpkg_path] # pragma: no cover
sys.modules[subpkg_path] = mock_subpkg # pragma: no cover
module_name = 'module' # pragma: no cover
module_path = f'{subpkg_path}.{module_name}' # pragma: no cover
mock_module = types.ModuleType(module_path) # pragma: no cover
sys.modules[module_path] = mock_module # pragma: no cover
    return sys.modules[name] # pragma: no cover
def mock_iter_modules(paths): # pragma: no cover
    if paths == [path]: # pragma: no cover
        yield None, subpkg_name, True # pragma: no cover
    elif paths == [subpkg_path]: # pragma: no cover
        yield None, module_name, False # pragma: no cover
globals()['iter_modules'] = mock_iter_modules # pragma: no cover
def walk_modules(fullpath): # pragma: no cover
    mods = [] # pragma: no cover
    mods.append(mod) # pragma: no cover
    if hasattr(mod, '__path__'):  # pragma: no cover
        for _, subpath, ispkg in iter_modules(mod.__path__): # pragma: no cover
            if ispkg: # pragma: no cover
                mods += walk_modules(f'{fullpath}.{subpath}') # pragma: no cover
            else: # pragma: no cover
    return mods # pragma: no cover
    print([mod.__name__ for mod in modules]) # pragma: no cover

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
