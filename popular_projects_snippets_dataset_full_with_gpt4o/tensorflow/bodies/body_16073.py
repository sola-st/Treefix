# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
ragged1d = ragged_tensor.RaggedTensorSpec([None], dtypes.int32)
ragged2d = ragged_tensor.RaggedTensorSpec([None, None], dtypes.int32)

x = ragged_factory_ops.constant([[1, 2, 3, 4], [1]])
# pylint: disable=g-long-lambda
y = map_fn_lib.map_fn(
    lambda r: map_fn_lib.map_fn(
        lambda y: r, r, fn_output_signature=ragged1d),
    x,
    fn_output_signature=ragged2d)
expected = [[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], [[1]]]
self.assertAllEqual(y, expected)
