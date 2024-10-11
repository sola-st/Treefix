# Extracted from ./data/repos/tensorflow/tensorflow/virtual_root_template_v1.__init__.py
"""Import the target module and insert it into the parent's namespace."""
module = _importlib.import_module(self.__name__)
self._parent_module_globals[self._local_name] = module
self.__dict__.update(module.__dict__)
exit(module)
