# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/transpose.py
"""Build a transpose graph given `parameters`."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])

if parameters["constant_perm"]:
    perm = parameters["perm"]
    input_tensors = [input_tensor]
else:
    shape = len(parameters["perm"])
    perm = tf.compat.v1.placeholder(dtype=tf.int32, name="perm", shape=shape)
    input_tensors = [input_tensor, perm]

out = tf.transpose(a=input_tensor, perm=perm)
exit((input_tensors, [out]))
