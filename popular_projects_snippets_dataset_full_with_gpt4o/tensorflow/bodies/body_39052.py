# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
with self.session(use_gpu=False) as sess:
    sp_input = self._SparseTensorPlaceholder()
    input0_val = self._SparseTensorValue_5x6(np.arange(6))
    input1_val = self._SparseTensorValue_1x1x1()
    handle = add_sparse_to_tensors_map(sp_input)

    handle0_value = sess.run(handle, feed_dict={sp_input: input0_val})
    handle1_value = sess.run(handle, feed_dict={sp_input: input1_val})

    handle_concat = ops.convert_to_tensor(
        [handle0_value, handle1_value], dtype=dtypes.int64)

    sp_roundtrip = take_many_sparse_from_tensors_map(
        sparse_map_op=handle.op, sparse_handles=handle_concat)

    with self.assertRaisesOpError(
        r"Inconsistent rank across SparseTensors: rank prior to "
        r"SparseTensor\[1\] was: 3 but rank of SparseTensor\[1\] is: 4"):
        self.evaluate(sp_roundtrip)
