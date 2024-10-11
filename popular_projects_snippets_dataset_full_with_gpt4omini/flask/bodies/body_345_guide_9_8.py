import importlib.util # pragma: no cover
import os # pragma: no cover
import pathlib # pragma: no cover
import pkgutil # pragma: no cover

class MockLoader: # pragma: no cover
    def get_filename(self, name): # pragma: no cover
        return '/path/to/example_namespace/__init__.py' # pragma: no cover
    @property # pragma: no cover
    def submodule_search_locations(self): # pragma: no cover
        return ['/path/to/example_namespace'] # pragma: no cover
loader = MockLoader() # pragma: no cover
class MockSpec: # pragma: no cover
    def __init__(self, origin, submodule_search_locations): # pragma: no cover
        self.origin = origin if origin is not None else 'namespace' # pragma: no cover
        self.submodule_search_locations = submodule_search_locations # pragma: no cover
root_spec = MockSpec('namespace', ['/path/to/example_namespace']) # pragma: no cover
def _path_is_relative_to(package_path, location): # pragma: no cover
    return str(location).startswith(str(package_path)) # pragma: no cover
def _matching_loader_thinks_module_is_package(loader, name): # pragma: no cover
    return True # pragma: no cover
class MockPackageSpec: # pragma: no cover
    def __init__(self, submodule_search_locations): # pragma: no cover
        self.submodule_search_locations = submodule_search_locations # pragma: no cover
package_spec = MockPackageSpec(['/path/to/example_namespace']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Find the path that contains the package or module."""
root_mod_name, _, _ = import_name.partition(".")
_l_(7627)

try:
    _l_(7643)

    root_spec = importlib.util.find_spec(root_mod_name)
    _l_(7628)

    if root_spec is None:
        _l_(7630)

        raise ValueError("not found")
        _l_(7629)
except (ImportError, ValueError):
    _l_(7632)

    pass  # handled below
    _l_(7631)  # handled below
else:
    # namespace package
    if root_spec.origin in {"namespace", None}:
        _l_(7642)

        package_spec = importlib.util.find_spec(import_name)
        _l_(7633)
        if package_spec is not None and package_spec.submodule_search_locations:
            _l_(7637)

            # Pick the path in the namespace that contains the submodule.
            package_path = pathlib.Path(
                os.path.commonpath(package_spec.submodule_search_locations)
            )
            _l_(7634)
            search_locations = (
                location
                for location in root_spec.submodule_search_locations
                if _path_is_relative_to(package_path, location)
            )
            _l_(7635)
        else:
            # Pick the first path.
            search_locations = iter(root_spec.submodule_search_locations)
            _l_(7636)
        aux = os.path.dirname(next(search_locations))
        _l_(7638)
        exit(aux)
    # a package (with __init__.py)
    elif root_spec.submodule_search_locations:
        _l_(7641)

        aux = os.path.dirname(os.path.dirname(root_spec.origin))
        _l_(7639)
        exit(aux)
    # just a normal module
    else:
        aux = os.path.dirname(root_spec.origin)
        _l_(7640)
        exit(aux)

    # we were unable to find the `package_path` using PEP 451 loaders
loader = pkgutil.get_loader(root_mod_name)
_l_(7644)

if loader is None or root_mod_name == "__main__":
    _l_(7646)

    aux = os.getcwd()
    _l_(7645)
    # import name is not found, or interactive/main module
    exit(aux)

if hasattr(loader, "get_filename"):
    _l_(7651)

    filename = loader.get_filename(root_mod_name)
    _l_(7647)
elif hasattr(loader, "archive"):
    _l_(7650)

    # zipimporter's loader.archive points to the .egg or .zip file.
    filename = loader.archive
    _l_(7648)
else:
    # At least one loader is missing both get_filename and archive:
    # Google App Engine's HardenedModulesHook, use __file__.
    filename = importlib.import_module(root_mod_name).__file__
    _l_(7649)

package_path = os.path.abspath(os.path.dirname(filename))
_l_(7652)

# If the imported name is a package, filename is currently pointing
# to the root of the package, need to get the current directory.
if _matching_loader_thinks_module_is_package(loader, root_mod_name):
    _l_(7654)

    package_path = os.path.dirname(package_path)
    _l_(7653)
aux = package_path
_l_(7655)

exit(aux)
