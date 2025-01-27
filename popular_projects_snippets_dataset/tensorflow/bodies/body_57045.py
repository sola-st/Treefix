# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/l2norm_shared_epsilon.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
epsilon = tf.constant(parameters["epsilon"])
out1 = tf.nn.l2_normalize(input_tensor, parameters["dim"], epsilon=epsilon)
out2 = tf.nn.l2_normalize(input_tensor, parameters["dim"], epsilon=epsilon)
out = out1 + out2
exit(([input_tensor], [out]))
