# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/strided_slice.py
"""Build inputs for stride_slice test."""
input_values = create_tensor_data(
    parameters["dtype"],
    parameters["input_shape"],
    min_value=-1,
    max_value=1)
index_type = MAP_TF_TO_NUMPY_TYPE[parameters["index_type"]]
values = [input_values]
if not parameters["constant_indices"]:
    begin_values = np.array(parameters["begin"]).astype(index_type)
    end_values = np.array(parameters["end"]).astype(index_type)
    stride_values = (
        np.array(parameters["strides"]).astype(index_type)
        if parameters["strides"] is not None else None)
    values.append(begin_values)
    values.append(end_values)
    if stride_values is not None:
        values.append(stride_values)

exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
