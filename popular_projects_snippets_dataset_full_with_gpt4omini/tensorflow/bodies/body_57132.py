# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/mirror_pad.py
if not parameters["fully_quantize"]:
    input_values = [create_tensor_data(tf.float32, parameters["input_shape"])]
else:
    input_values = [
        create_tensor_data(
            tf.float32, parameters["input_shape"], min_value=-1, max_value=1)
    ]
if parameters["type"] != "const":
    input_values.append(np.array(parameters["padding_matrix"]))
exit((input_values, sess.run(
    outputs, feed_dict=dict(zip(inputs, input_values)))))
