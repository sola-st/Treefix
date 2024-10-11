# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
with self.session() as sess:
    with self.test_scope():
        seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
        x = stateless_random_ops.stateless_multinomial(
            array_ops.zeros([42, 40]),
            0,
            seed=seed_t,
            output_dtype=dtypes.int32)
        y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
        self.assertEqual(y.shape, (42, 0))
