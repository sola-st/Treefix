# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pack.py
all_values = []
for _ in range(0, parameters["num_tensors"]):
    input_values = create_tensor_data(
        np.float32, get_shape(parameters), min_value=-1, max_value=1)
    all_values.append(input_values)
exit((all_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, all_values)))))
