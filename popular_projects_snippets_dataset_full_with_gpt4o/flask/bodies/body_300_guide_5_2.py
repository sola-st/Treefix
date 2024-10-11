import sys # pragma: no cover
import os # pragma: no cover
import pkgutil # pragma: no cover

class MockLoader: # pragma: no cover
    def get_filename(self, name): # pragma: no cover
        return '/path/to/example_package/__init__.py' # pragma: no cover
pkgutil.get_loader = lambda name: MockLoader() if name == 'example_package' else None # pragma: no cover
sys.modules['example_package'] = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
"""Find the root path of a package, or the path that contains a
    module. If it cannot be found, returns the current working
    directory.

    Not to be confused with the value returned by :func:`find_package`.

    :meta private:
    """
# Module already imported and has a file attribute. Use that first.
mod = sys.modules.get(import_name)
_l_(19400)

if mod is not None and hasattr(mod, "__file__") and mod.__file__ is not None:
    _l_(19402)

    aux = os.path.dirname(os.path.abspath(mod.__file__))
    _l_(19401)
    exit(aux)

# Next attempt: check the loader.
loader = pkgutil.get_loader(import_name)
_l_(19403)

# Loader does not exist or we're referring to an unloaded main
# module or a main module without path (interactive sessions), go
# with the current working directory.
if loader is None or import_name == "__main__":
    _l_(19405)

    aux = os.getcwd()
    _l_(19404)
    exit(aux)

if hasattr(loader, "get_filename"):
    _l_(19412)

    filepath = loader.get_filename(import_name)
    _l_(19406)
else:
    # Fall back to imports.
    __import__(import_name)
    _l_(19407)
    mod = sys.modules[import_name]
    _l_(19408)
    filepath = getattr(mod, "__file__", None)
    _l_(19409)

    # If we don't have a file path it might be because it is a
    # namespace package. In this case pick the root path from the
    # first module that is contained in the package.
    if filepath is None:
        _l_(19411)

        raise RuntimeError(
            "No root path can be found for the provided module"
            f" {import_name!r}. This can happen because the module"
            " came from an import hook that does not provide file"
            " name information or because it's a namespace package."
            " In this case the root path needs to be explicitly"
            " provided."
        )
        _l_(19410)

    # filepath is import_name.py for a module, or __init__.py for a package.
aux = os.path.dirname(os.path.abspath(filepath))
_l_(19413)
exit(aux)
