# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int64)])
def fun(x):
    shape_a = DynamicRaggedShape([], array_ops.stack([5, x, 3]))
    shape_b = DynamicRaggedShape.from_lengths([1, 3], dtype=dtypes.int64)
    result = dynamic_ragged_shape.broadcast_dynamic_shape(shape_a, shape_b)
    self.assertAllEqual([5, None, 3], result.static_lengths())
fun(constant_op.constant(2, dtype=dtypes.int64))
