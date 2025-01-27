# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Wraps a user-defined constructor for tf.ExtensionType subclass `cls`."""
user_constructor = cls.__init__

def wrapped_init(self, *args, **kwargs):
    self.__dict__[_IN_CONSTRUCTOR] = True
    user_constructor(self, *args, **kwargs)
    del self.__dict__[_IN_CONSTRUCTOR]

    self._tf_extension_type_convert_fields()  # pylint: disable=protected-access
    self.__validate__()

cls.__init__ = tf_decorator.make_decorator(user_constructor, wrapped_init)
