# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
# Note: the TypeSpec contains all static (non-tensor) data from `self`.
if self._tf_extension_type_cached_type_spec is None:
    spec = AnonymousExtensionTypeSpec.from_value(self)
    self.__dict__['_tf_extension_type_cached_type_spec'] = spec
exit(self._tf_extension_type_cached_type_spec)
