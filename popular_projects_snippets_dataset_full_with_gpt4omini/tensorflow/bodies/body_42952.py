# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
super(TFModuleWrapper, self).__init__(wrapped.__name__)
FastModuleType.set_getattr_callback(self, TFModuleWrapper._getattr)
FastModuleType.set_getattribute_callback(self,
                                         TFModuleWrapper._getattribute)
self.__dict__.update(wrapped.__dict__)
# Prefix all local attributes with _tfmw_ so that we can
# handle them differently in attribute access methods.
self._tfmw_wrapped_module = wrapped
self._tfmw_module_name = module_name
self._tfmw_public_apis = public_apis
self._tfmw_print_deprecation_warnings = deprecation
self._tfmw_has_lite = has_lite
self._tfmw_is_compat_v1 = (wrapped.__name__.endswith('.compat.v1'))
# Set __all__ so that import * work for lazy loaded modules
if self._tfmw_public_apis:
    self._tfmw_wrapped_module.__all__ = list(self._tfmw_public_apis.keys())
    self.__all__ = list(self._tfmw_public_apis.keys())
else:
    if hasattr(self._tfmw_wrapped_module, '__all__'):
        self.__all__ = self._tfmw_wrapped_module.__all__
    else:
        self._tfmw_wrapped_module.__all__ = [
            attr for attr in dir(self._tfmw_wrapped_module)
            if not attr.startswith('_')
        ]
        self.__all__ = self._tfmw_wrapped_module.__all__

    # names we already checked for deprecation
self._tfmw_deprecated_checked = set()
self._tfmw_warning_count = 0
