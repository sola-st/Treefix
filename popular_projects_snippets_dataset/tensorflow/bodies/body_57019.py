# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/concat.py
all_values = []
for n in range(0, parameters["num_tensors"]):
    input_values = create_tensor_data(
        parameters["type"],
        get_shape(parameters, n),
        min_value=-1,
        max_value=1)
    all_values.append(input_values)
exit((all_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, all_values)))))
