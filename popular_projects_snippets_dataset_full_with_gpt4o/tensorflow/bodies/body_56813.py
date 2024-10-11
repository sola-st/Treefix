# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cumsum.py
input1 = create_tensor_data(parameters["dtype"], parameters["shape"])
exit(([input1], sess.run(outputs, feed_dict=dict(zip(inputs, [input1])))))
