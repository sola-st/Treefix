# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sigmoid_grad.py
y = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="y", shape=parameters["input_shape"])
dy = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="dy", shape=parameters["input_shape"])
out = tf.raw_ops.SigmoidGrad(y=y, dy=dy)
exit(([y, dy], [out]))
