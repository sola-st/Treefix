# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
elems = ragged_factory_ops.constant([[1, 2, 3], [4, 5], [6, 7]])
fn = lambda x: ragged_tensor.RaggedTensor.from_row_starts(x, [0])
with self.assertRaisesRegex(
    ValueError, r'(?s)Expected `fn` to return.*But it returned.*'):
    _ = ragged_map_ops.map_fn(
        fn,
        elems,
        dtype=ragged_tensor.RaggedTensorType(
            dtype=dtypes.int64, ragged_rank=10))
