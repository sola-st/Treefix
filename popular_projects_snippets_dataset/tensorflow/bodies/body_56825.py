# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/range.py
input_value = create_scalar_data(parameters["dtype"])
exit(([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))))
