# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pack.py
all_tensors = []
for n in range(0, parameters["num_tensors"]):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name=("input%d" % n),
        shape=get_shape(parameters))
    all_tensors.append(input_tensor)
out = tf.stack(all_tensors, parameters["axis"])
exit((all_tensors, [out]))
