# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
var = variables.VariableV1(np.zeros((5, 5), np.float32), name="noop")
self.assertEqual(
    "<tf.Variable 'noop:0' shape=(5, 5) dtype=float32_ref>",
    repr(var))
