# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
for dtype in self.float_types:
    for output_dtype in self.output_dtypes():
        with self.session():
            with self.test_scope():
                x = random_ops.multinomial(
                    array_ops.ones(shape=[1, 20], dtype=dtype), 1000,
                    output_dtype=output_dtype)
            y = self.evaluate(x)
            self.assertTrue((y >= 0).sum() == 1000)
            self.assertTrue((y < 20).sum() == 1000)
