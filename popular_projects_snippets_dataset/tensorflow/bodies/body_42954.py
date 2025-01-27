# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
"""Lazily loading the modules."""
# We ignore 'app' because it is accessed in __init__.py of tf.compat.v1.
# That way, if a user only imports tensorflow.compat.v1, it is not
# considered v1 API usage.
if (self._tfmw_is_compat_v1 and name != 'app' and
    not TFModuleWrapper.compat_v1_usage_recorded):
    TFModuleWrapper.compat_v1_usage_recorded = True
    compat_v1_usage_gauge.get_cell().set(True)

symbol_loc_info = self._tfmw_public_apis[name]
if symbol_loc_info[0]:
    module = importlib.import_module(symbol_loc_info[0])
    attr = getattr(module, symbol_loc_info[1])
else:
    attr = importlib.import_module(symbol_loc_info[1])
setattr(self._tfmw_wrapped_module, name, attr)
self.__dict__[name] = attr
# Cache the pair
self._fastdict_insert(name, attr)
exit(attr)
