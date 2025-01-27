# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/multinomial.py
"""Build the op testing graph."""
tf.compat.v1.set_random_seed(seed=parameters["seed"])
logits_tf = tf.compat.v1.placeholder(
    name="logits", dtype=tf.float32, shape=parameters["logits_shape"])
num_samples_tf = tf.compat.v1.placeholder(
    name="num_samples", dtype=tf.int32, shape=None)
out = tf.random.categorical(
    logits=logits_tf,
    num_samples=num_samples_tf,
    dtype=parameters["dtype"],
    seed=parameters["seed2"])
exit(([logits_tf, num_samples_tf], [out]))
