# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
exit(random_ops.multinomial(np.array([[1., 1., 1.]], dtype=dtype), 10,
                              output_dtype=output_dtype))
