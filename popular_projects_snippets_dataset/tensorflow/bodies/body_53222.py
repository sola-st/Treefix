# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Builds a constructor for ExtensionTypeSpec subclass `cls`."""
params = []
kind = tf_inspect.Parameter.POSITIONAL_OR_KEYWORD
for field in cls._tf_extension_type_fields():  # pylint: disable=protected-access
    params.append(tf_inspect.Parameter(field.name, kind))

signature = tf_inspect.Signature(params, return_annotation=cls.__name__)

def __init__(self, *args, **kwargs):  # pylint: disable=invalid-name
    bound_args = signature.bind(*args, **kwargs)
    bound_args.apply_defaults()
    self.__dict__.update(bound_args.arguments)
    self._tf_extension_type_convert_fields()  # pylint: disable=protected-access
    self.__validate__()

# __signature__ is supported by some inspection/documentation tools.
__init__.__signature__ = tf_inspect.Signature(
    [
        tf_inspect.Parameter('self',
                             tf_inspect.Parameter.POSITIONAL_OR_KEYWORD)
    ] + params,
    return_annotation=cls)

cls.__init__ = __init__
