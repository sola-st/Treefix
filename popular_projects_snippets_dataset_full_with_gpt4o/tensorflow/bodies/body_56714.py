# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/strided_slice_np_style.py
input_value = create_tensor_data(parameters["dtype"], parameters["shape"])
exit(([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value])))))
