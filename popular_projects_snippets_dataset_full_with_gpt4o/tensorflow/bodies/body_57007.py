# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/where_v2.py
input_condition = create_tensor_data(parameters["condition_dtype"],
                                     parameters["input_condition_shape"])
input_value1 = None
input_value2 = None
if parameters["input_dtype"] is not None:
    input_value1 = create_tensor_data(
        parameters["input_dtype"],
        build_input_shape(parameters["input_shape_set"][0]))
    input_value2 = create_tensor_data(
        parameters["input_dtype"],
        build_input_shape(parameters["input_shape_set"][1]))
    exit(([input_condition, input_value1, input_value2], sess.run(
        outputs,
        feed_dict=dict(
            zip(inputs, [input_condition, input_value1, input_value2])))))
else:
    exit(([input_condition, input_value1, input_value2], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_condition])))))
