# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
self.__dict__[_IN_CONSTRUCTOR] = True
user_constructor(self, *args, **kwargs)
del self.__dict__[_IN_CONSTRUCTOR]

self._tf_extension_type_convert_fields()  # pylint: disable=protected-access
self.__validate__()
