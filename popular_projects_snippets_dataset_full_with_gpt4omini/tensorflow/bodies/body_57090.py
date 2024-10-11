# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather.py
input_values = []
min_value, max_value = parameters.get("input_range", (-10, 10))
if not parameters["constant_params"]:
    params = create_tensor_data(
        parameters["params_dtype"],
        parameters["params_shape"],
        min_value=min_value,
        max_value=max_value)
    input_values.append(params)
if not parameters.get("constant_indices", False):
    indices = create_tensor_data(
        parameters["indices_dtype"],
        parameters["indices_shape"],
        min_value=0,
        max_value=parameters["params_shape"][0] - 1)
    input_values.append(indices)
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
