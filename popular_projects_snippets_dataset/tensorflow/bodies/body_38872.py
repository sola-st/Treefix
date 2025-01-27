# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session() as sess:
    dtypes = [dtypes_lib.float16, dtypes_lib.float32, dtypes_lib.float64]

    for i in range(len(dtypes)):
        dtype = dtypes[i]
        q = data_flow_ops.SparseConditionalAccumulator(
            dtype, shape=tensor_shape.TensorShape([3, 3, 3]))

        elems = np.arange(2)
        sum_elems = np.zeros([3, 3, 3]).astype(dtype.as_numpy_dtype)
        for e in elems:
            mat_to_add = np.zeros([3, 3, 3]).astype(dtype.as_numpy_dtype)
            mat_to_add[i, i, i] = e + 1
            sum_elems += mat_to_add
            t = _indexedslice(mat_to_add)
            q.apply_indexed_slices_grad(t).run()

        result = self.evaluate(q.take_indexed_slices_grad(1))

        self._assertEqual_nparray(sum_elems / len(elems), result, sess)
