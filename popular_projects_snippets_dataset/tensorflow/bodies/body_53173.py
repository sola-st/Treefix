# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if (name in _MUTABLE_KERAS_PROPERTIES or
    (hasattr(self, _IN_CONSTRUCTOR) and
     self._tf_extension_type_has_field(name))):
    del self.__dict__[name]
else:
    raise AttributeError(f'Cannot mutate attribute `{name}` '
                         f'outside the custom constructor of ExtensionType.')
