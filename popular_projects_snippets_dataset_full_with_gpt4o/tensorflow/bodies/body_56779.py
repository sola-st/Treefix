# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/l2norm.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
if parameters["epsilon"]:
    out = tf.nn.l2_normalize(
        input_tensor, parameters["dim"], epsilon=parameters["epsilon"])
else:
    out = tf.nn.l2_normalize(input_tensor, parameters["dim"])
exit(([input_tensor], [out]))
