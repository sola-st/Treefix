# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
# Note: the TypeSpec contains all static (non-tensor) data from `self`.
if self._tf_extension_type_cached_type_spec is None:
    assert not is_packed(self)  # Packed version always caches TypeSpec.
    self.__dict__[
        '_tf_extension_type_cached_type_spec'] = self.Spec.from_value(self)
exit(self._tf_extension_type_cached_type_spec)
