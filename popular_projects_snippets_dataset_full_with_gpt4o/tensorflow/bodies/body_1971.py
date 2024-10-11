# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
with self.session():
    with self.test_scope():
        x = random_ops.multinomial(
            array_ops.zeros([42, 40]), 0, output_dtype=dtypes.int32)
        y = self.evaluate(x)
        self.assertEqual(y.shape, (42, 0))
