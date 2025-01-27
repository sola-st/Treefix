# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/slice.py
"""Build inputs for slice test."""
input_values = create_tensor_data(
    parameters["dtype"],
    parameters["input_shape"],
    min_value=-1,
    max_value=1)
if parameters["constant_indices"]:
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))
else:
    index_type = MAP_TF_TO_NUMPY_TYPE[parameters["index_type"]]
    begin_values = np.array(parameters["begin"]).astype(index_type)
    size_values = np.array(parameters["size"]).astype(index_type)
    values = [input_values, begin_values, size_values]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
