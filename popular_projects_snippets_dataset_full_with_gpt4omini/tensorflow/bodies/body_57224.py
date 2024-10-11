# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/parse_example.py
feature_dtype = parameters["feature_dtype"]
feature_shape = parameters["feature_shape"]
input_values = [create_example_data(feature_dtype, feature_shape)]
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
