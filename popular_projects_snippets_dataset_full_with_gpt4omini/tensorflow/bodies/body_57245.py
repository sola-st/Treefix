# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/static_hashtable.py
(key_dtype, _, _, _, _) = parameters["table"]
input_values = [create_tensor_data(key_dtype, parameters["input_shape"])]
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
