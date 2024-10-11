# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/transpose.py
values = [
    create_tensor_data(parameters["dtype"], parameters["input_shape"],
                       min_value=-1, max_value=1)
]
if not parameters["constant_perm"]:
    values.append(np.array(parameters["perm"]))
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
