# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def foo(inner_shape):
    a = DynamicRaggedShape([RowPartition.from_row_lengths([3, 3])],
                           inner_shape)
    actual = a._to_tensor_shape()
    self.assertDimsEqual(
        tensor_shape.TensorShape(None), actual)

foo([6, 3])
