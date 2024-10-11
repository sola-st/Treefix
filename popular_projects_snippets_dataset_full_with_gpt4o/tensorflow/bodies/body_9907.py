# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
self._output_package = output_package
# Maps API module to API symbol name to set of tuples of the form
# (module name, priority).
# The same symbol can be imported from multiple locations. Higher
# "priority" indicates that import location is preferred over others.
self._module_imports = collections.defaultdict(
    lambda: collections.defaultdict(set))
self._dest_import_to_id = collections.defaultdict(int)
# Names that start with underscore in the root module.
self._underscore_names_in_root = set()
self._api_version = api_version
# Controls whether or not exported symbols are lazily loaded or statically
# imported.
self._lazy_loading = lazy_loading
self._use_relative_imports = use_relative_imports
