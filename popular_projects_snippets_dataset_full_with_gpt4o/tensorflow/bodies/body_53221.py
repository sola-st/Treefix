# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
bound_args = signature.bind(*args, **kwargs)
bound_args.apply_defaults()
self.__dict__.update(bound_args.arguments)
self._tf_extension_type_convert_fields()  # pylint: disable=protected-access
self.__validate__()
