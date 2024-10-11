# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
with self.session(use_gpu=False) as sess:
    input_val = self._SparseTensorValue_5x6(np.arange(6))
    handle = add_sparse_to_tensors_map(input_val)
    handle_value = self.evaluate(handle)
    bad_handle = handle_value + 10
    sp_roundtrip = take_many_sparse_from_tensors_map(
        sparse_map_op=handle.op, sparse_handles=[handle_value, bad_handle])

    with self.assertRaisesOpError(r"Unable to find SparseTensor: 10"):
        self.evaluate(sp_roundtrip)
