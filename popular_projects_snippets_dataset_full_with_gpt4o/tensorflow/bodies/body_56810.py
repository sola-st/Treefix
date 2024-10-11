# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/batch_to_space_nd.py
values = [
    create_tensor_data(parameters["dtype"], parameters["input_shape"])
]
if not parameters["constant_block_shape"]:
    values.append(np.array(parameters["block_shape"]))
if not parameters["constant_crops"]:
    values.append(np.array(parameters["crops"]))
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
