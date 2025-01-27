# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
x = ragged_factory_ops.constant(
    [[10, 20], [30, 40], [50, 60], [70], [80, 90, 100]], dtypes.int64)
y = array_ops.expand_dims(mo.range(x.nrows(out_type=dtypes.int64)), axis=1)

def _zip(foo):
    y_val, x_val = foo
    bar = array_ops.tile(y_val, array_ops.shape(x_val))
    exit(array_ops.stack([bar, x_val], axis=1))

output = ragged_map_ops.map_fn(
    _zip, (y, x),
    dtype=ragged_tensor.RaggedTensorType(dtype=dtypes.int64, ragged_rank=1),
    infer_shape=False)

self.assertAllEqual(
    output, [[[0, 10], [0, 20]], [[1, 30], [1, 40]], [[2, 50], [2, 60]],
             [[3, 70]], [[4, 80], [4, 90], [4, 100]]])
