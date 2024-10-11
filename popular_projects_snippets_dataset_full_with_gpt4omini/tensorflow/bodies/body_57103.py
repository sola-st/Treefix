# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/local_response_norm.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.nn.local_response_normalization(
    input_tensor,
    depth_radius=parameters["depth_radius"],
    bias=parameters["bias"],
    alpha=parameters["alpha"],
    beta=parameters["beta"])
exit(([input_tensor], [out]))
