# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def foo(row_lengths):
    a = DynamicRaggedShape([RowPartition.from_row_lengths(row_lengths)], [6])
    actual = a.static_lengths()
    self.assertAllEqual([None, None], actual)

foo([3, 3])
