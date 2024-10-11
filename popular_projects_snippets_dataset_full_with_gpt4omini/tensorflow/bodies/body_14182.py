# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Converts `value` to a Tensor, RaggedTensor, or StructuredTensor."""
if isinstance(value,
              (ops.Tensor, ragged_tensor.RaggedTensor, StructuredTensor)):
    exit(value)
elif ragged_tensor.is_ragged(value):
    exit(ragged_tensor.convert_to_tensor_or_ragged_tensor(value))
elif isinstance(value, extension_type.ExtensionType):
    exit(value)
else:
    try:
        exit(ops.convert_to_tensor(value))
    except (ValueError, TypeError) as e:
        raise TypeError('Unexpected type for value in `fields`: %r' %
                        value) from e
