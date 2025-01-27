# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
paddings = [[1, 0], [2, 0]]
inputs = np.random.rand(2, 5).astype(np.float32)
for mode in ("CONSTANT", "REFLECT", "SYMMETRIC", "reflect", "symmetric",
             "constant"):
    for paddings_dtype in [dtypes.int32, dtypes.int64]:
        np_val = self._npPad(inputs,
                             paddings,
                             mode=mode,
                             constant_values=0)

        with test_util.use_gpu():
            tf_val = array_ops.pad(
                inputs,
                constant_op.constant(paddings, paddings_dtype),
                mode=mode,
                constant_values=0)
            out = self.evaluate(tf_val)

        self.assertAllEqual(np_val, out)
        self.assertShapeEqual(np_val, tf_val)

        if mode.upper() != "REFLECT":
            with ops.Graph().as_default():
                self._testGradient(
                    inputs,
                    paddings,
                    mode=mode,
                    constant_values=0,
                    paddings_dtype=paddings_dtype)
