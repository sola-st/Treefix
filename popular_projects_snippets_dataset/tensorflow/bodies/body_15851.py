# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Note that the rank of the shape is unknown, so we can only provide a
# prefix of the lengths.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def foo(inner_shape):
    a = DynamicRaggedShape([RowPartition.from_row_lengths([3, 3])],
                           inner_shape)
    actual = a.static_lengths()
    self.assertAllEqual([2, (3, 3), ...], actual)

foo([6, 3])
