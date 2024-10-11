# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unroll_batch_matmul.py
input_value1 = create_tensor_data(
    parameters["dtype"], shape=parameters["shape"][0])
input_value2 = create_tensor_data(
    parameters["dtype"], shape=parameters["shape"][1])
exit(([input_value1, input_value2], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))
