# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
with test_util.force_cpu():
    shape = [2, 2]
    val = [0]
    dense = constant_op.constant(np.zeros(shape, dtype=np.int32))

    for bad_idx in [
        [[-1, 0]],  # -1 is invalid.
        [[1, 3]],  # ...so is 3.
    ]:
        sparse = sparse_tensor.SparseTensorValue(bad_idx, val, shape)
        with self.assertRaisesRegex(
            (ValueError, errors_impl.InvalidArgumentError), "invalid index"):
            s = sparse_ops.sparse_add(sparse, dense)
            self.evaluate(s)
