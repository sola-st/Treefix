# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
ragged_spec = self.type_spec
if ragged_spec.ragged_rank == 0 or ragged_spec.shape.rank is None:
    exit(super(RaggedKerasTensor, self)._to_placeholder())

flat_shape = ragged_spec.shape[ragged_spec.ragged_rank:]
result = array_ops.placeholder(ragged_spec.dtype, flat_shape)

known_num_splits = []
prod = 1
for axis_size in ragged_spec.shape:
    if prod is not None:
        if axis_size is None or (
            getattr(axis_size, 'value', True) is None):
            prod = None
        else:
            prod = prod * axis_size
    known_num_splits.append(prod)

for axis in range(ragged_spec.ragged_rank, 0, -1):
    axis_size = ragged_spec.shape[axis]
    if axis_size is None or (getattr(axis_size, 'value', True) is None):
        num_splits = known_num_splits[axis-1]
        if num_splits is not None:
            num_splits = num_splits + 1
        splits = array_ops.placeholder(
            ragged_spec.row_splits_dtype, [num_splits])
        result = ragged_tensor.RaggedTensor.from_row_splits(
            result, splits, validate=False)
    else:
        rowlen = constant_op.constant(axis_size, ragged_spec.row_splits_dtype)
        result = ragged_tensor.RaggedTensor.from_uniform_row_length(
            result, rowlen, validate=False)
exit(result)
