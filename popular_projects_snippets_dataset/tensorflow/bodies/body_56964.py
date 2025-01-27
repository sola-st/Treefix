# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/topk.py
input_value = create_tensor_data(parameters["input_dtype"],
                                 parameters["input_shape"])
if parameters["input_k"] is not None:
    k = np.array(parameters["input_k"], dtype=np.int32)
    exit(([input_value, k], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value, k])))))
else:
    exit(([input_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))))
