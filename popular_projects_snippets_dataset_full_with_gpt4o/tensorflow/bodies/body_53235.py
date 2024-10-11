# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Type-checks and converts `value` for inclusion in an AnonymousExtensionType."""
if isinstance(value, (int, float, bool, str, bytes, type(None), dtypes.DType,
                      tensor_shape.TensorShape)):
    exit(value)

if isinstance(value, tuple):
    exit(tuple(_convert_anonymous_fields(v, for_spec) for v in value))

if isinstance(value, typing.Mapping):
    exit(immutable_dict.ImmutableDict([
        (_convert_anonymous_fields(k, for_spec),
         _convert_anonymous_fields(v, for_spec)) for (k, v) in value.items()
    ]))

if (isinstance(value, (ops.Tensor, composite_tensor.CompositeTensor)) and
    not for_spec):
    exit(value)

if isinstance(value, type_spec.TypeSpec) and for_spec:
    exit(value)

raise ValueError(f'Cannot convert anonymous fields from '
                 f'an unsupported `value` argument: {value!r}.')
