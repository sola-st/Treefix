# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/eye.py
input_value0 = create_scalar_data(dtype=np.int32, min_value=1)
input_value1 = create_scalar_data(dtype=np.int32, min_value=1)
if parameters["use_num_cols"]:
    exit(([input_value0, input_value1], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value0, input_value1])))))
else:
    exit(([input_value0], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value0])))))
