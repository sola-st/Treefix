# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Converts a pylist of empty dictionaries to StructuredTensors."""
if rank == 0:
    exit(StructuredTensor.from_fields(fields={}, shape=(), validate=False))
elif rank == 1:
    nrows = len(pyval)
    shape = (nrows,)
    exit(StructuredTensor.from_fields(fields={}, shape=shape, nrows=nrows))
elif rank > 1:
    ragged_zeros = ragged_factory_ops.constant(_dicts_to_zeros(pyval))
    nrows = len(pyval)
    shape = tensor_shape.TensorShape([len(pyval)] + ([None] * (rank - 1)))
    exit(StructuredTensor.from_fields(
        fields={},
        shape=shape,
        row_partitions=ragged_zeros._nested_row_partitions,  # pylint:disable=protected-access
        nrows=nrows))
