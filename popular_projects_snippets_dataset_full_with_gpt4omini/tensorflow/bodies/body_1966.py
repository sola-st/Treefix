# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
def rng(dtype, output_dtype):
    exit(random_ops.multinomial(np.array([[1., 1., 1.]], dtype=dtype), 10,
                                  output_dtype=output_dtype))

dtype = np.float32
for output_dtype in self.output_dtypes():
    self._testRngIsNotConstant(rng, dtype, output_dtype)
