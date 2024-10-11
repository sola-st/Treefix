# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/slice.py
"""Build graph for slice test."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
if parameters["constant_indices"]:
    index_type = MAP_TF_TO_NUMPY_TYPE[parameters["index_type"]]
    begin_values = np.array(parameters["begin"]).astype(index_type)
    size_values = np.array(parameters["size"]).astype(index_type)
    out = tf.slice(input_tensor, begin_values, size_values)
    exit(([input_tensor], [out]))
else:
    begin = tf.compat.v1.placeholder(
        dtype=parameters["index_type"],
        name="begin",
        shape=[len(parameters["input_shape"])])
    size = tf.compat.v1.placeholder(
        dtype=parameters["index_type"],
        name="size",
        shape=[len(parameters["input_shape"])])
    tensors = [input_tensor, begin, size]
    out = tf.slice(input_tensor, begin, size)
    exit((tensors, [out]))
