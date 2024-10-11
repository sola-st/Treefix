# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sigmoid_grad.py
# input is y which is sigmoid(x), hence it's range is between 0 to 1
y = create_tensor_data(
    parameters["dtype"],
    parameters["input_shape"],
    min_value=0,
    max_value=1)
min_value, max_value = parameters["input_range"]
dy = create_tensor_data(parameters["dtype"], parameters["input_shape"],
                        min_value, max_value)
values = [y, dy]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
