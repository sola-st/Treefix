# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session() as sess:
    dtypes = [dtypes_lib.float16, dtypes_lib.float32, dtypes_lib.float64]

    for i in range(len(dtypes)):
        dtype = dtypes[i]
        q = data_flow_ops.ConditionalAccumulator(
            dtype, shape=tensor_shape.TensorShape([1]))

        elems = np.arange(10).astype(dtype.as_numpy_dtype)
        for e in elems:
            q.apply_grad((e,)).run()

        result = self.evaluate(q.take_grad(1))

        self.assertEqual(sum(elems) / len(elems), result)
