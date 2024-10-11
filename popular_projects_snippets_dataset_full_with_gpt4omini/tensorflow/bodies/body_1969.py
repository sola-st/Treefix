# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
for dtype in self.float_types.intersection(
    [dtypes.float32, dtypes.bfloat16]):
    for output_dtype in self.output_dtypes():
        with self.session() as sess:
            with self.test_scope():
                seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
                x = stateless_random_ops.stateless_multinomial(
                    array_ops.ones(shape=[1, 20], dtype=dtype),
                    1000,
                    seed_t,
                    output_dtype=output_dtype)
            y = sess.run(x, {seed_t: [0x12345678, 0xabcdef12]})
            self.assertTrue((y >= 0).sum() == 1000)
            self.assertTrue((y < 20).sum() == 1000)
