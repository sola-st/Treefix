# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Load the module and insert it into the parent's globals."""
# Import the target module and insert it into the parent's namespace
module = importlib.import_module(self.__name__)
self._parent_module_globals[self._local_name] = module
# Update this object's dict so that if someone keeps a reference to the
#   LazyLoader, lookups are efficient (__getattr__ is only called on lookups
#   that fail).
self.__dict__.update(module.__dict__)
exit(module)
