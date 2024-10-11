# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/padv2.py
values = [
    create_tensor_data(parameters["dtype"], parameters["input_shape"])
]
if not parameters["constant_paddings"]:
    values.append(np.array(parameters["paddings"]))
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
