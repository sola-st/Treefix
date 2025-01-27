# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Builds a constructor for tf.ExtensionType subclass `cls`."""
fields = cls._tf_extension_type_fields()  # pylint: disable=protected-access

# Mark any no-default fields that follow default fields as keyword_only.
got_default = False
keyword_only_start = len(fields)
for i in range(len(fields)):
    if got_default:
        if fields[i].default is _NO_DEFAULT:
            keyword_only_start = i
            break
    elif fields[i].default is not _NO_DEFAULT:
        got_default = True

params = []
for i, field in enumerate(fields):
    if i < keyword_only_start:
        kind = tf_inspect.Parameter.POSITIONAL_OR_KEYWORD
    else:
        kind = tf_inspect.Parameter.KEYWORD_ONLY
    if field.default is _NO_DEFAULT:
        default = tf_inspect.Parameter.empty
    else:
        default = field.default
    params.append(
        tf_inspect.Parameter(
            field.name, kind, default=default, annotation=field.value_type))

signature = tf_inspect.Signature(params, return_annotation=cls.__name__)

def __init__(self, *args, **kwargs):  # pylint: disable=invalid-name
    bound_args = signature.bind(*args, **kwargs)
    bound_args.apply_defaults()
    self.__dict__.update(bound_args.arguments)
    self._tf_extension_type_convert_fields()  # pylint: disable=protected-access
    self.__validate__()

# __signature__ is supported by some inspection/documentation tools
# (but note: typing.get_type_hints does not respect __signature__).
__init__.__signature__ = tf_inspect.Signature(
    [
        tf_inspect.Parameter('self',
                             tf_inspect.Parameter.POSITIONAL_OR_KEYWORD)
    ] + params,
    return_annotation=cls)

cls.__init__ = __init__
