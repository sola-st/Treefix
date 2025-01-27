# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/random_standard_normal.py
"""Build the op testing graph."""
tf.compat.v1.set_random_seed(seed=parameters["seed"])
input_value = tf.compat.v1.placeholder(
    name="shape",
    shape=parameters["input_shape"],
    dtype=parameters["input_dtype"])
out = tf.random.normal(
    shape=input_value, dtype=parameters["dtype"], seed=parameters["seed2"])
exit(([input_value], [out]))
