# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/strided_slice.py
"""Build graph for stride_slice test."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
if parameters["constant_indices"]:
    begin = parameters["begin"]
    end = parameters["end"]
    strides = parameters["strides"]
    tensors = [input_tensor]
else:
    begin = tf.compat.v1.placeholder(
        dtype=parameters["index_type"],
        name="begin",
        shape=[len(parameters["begin"])])
    end = tf.compat.v1.placeholder(
        dtype=parameters["index_type"],
        name="end",
        shape=[len(parameters["end"])])
    strides = None
    if parameters["strides"] is not None:
        strides = tf.compat.v1.placeholder(
            dtype=parameters["index_type"],
            name="strides",
            shape=[len(parameters["strides"])])
    tensors = [input_tensor, begin, end]
    if strides is not None:
        tensors.append(strides)

kwargs = {}
if parameters.get("ellipsis_mask", None):
    kwargs.update({"ellipsis_mask": parameters["ellipsis_mask"]})
if parameters.get("new_axis_mask", None):
    kwargs.update({"new_axis_mask": parameters["new_axis_mask"]})

out = tf.strided_slice(
    input_tensor,
    begin,
    end,
    strides,
    begin_mask=parameters["begin_mask"],
    end_mask=parameters["end_mask"],
    shrink_axis_mask=parameters["shrink_axis_mask"],
    **kwargs)
exit((tensors, [out]))
