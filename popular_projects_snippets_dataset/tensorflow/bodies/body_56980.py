# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pool3d.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = pool_op(
    input_tensor,
    ksize=parameters["ksize"],
    strides=parameters["strides"],
    data_format=parameters["data_format"],
    padding=parameters["padding"])
exit(([input_tensor], [out]))
