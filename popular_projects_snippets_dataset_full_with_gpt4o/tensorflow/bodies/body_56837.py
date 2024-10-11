# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/shape_to_strided_slice.py
"""Build graph for shape_stride_slice test."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["dynamic_input_shape"])
begin = parameters["begin"]
end = parameters["end"]
strides = parameters["strides"]
tensors = [input_tensor]
out = tf.strided_slice(
    tf.shape(input=input_tensor),
    begin,
    end,
    strides,
    begin_mask=parameters["begin_mask"],
    end_mask=parameters["end_mask"])
exit((tensors, [out]))
