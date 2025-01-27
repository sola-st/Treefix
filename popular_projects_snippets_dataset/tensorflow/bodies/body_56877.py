# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tile.py
min_value, max_value = parameters.get("input_range", (-10, 10))
input_value = create_tensor_data(
    parameters["input_dtype"],
    parameters["input_shape"],
    min_value=min_value,
    max_value=max_value)
multipliers_value = create_tensor_data(
    parameters["multiplier_dtype"],
    parameters["multiplier_shape"],
    min_value=0)
exit(([input_value, multipliers_value], sess.run(
    outputs,
    feed_dict={
        inputs[0]: input_value,
        inputs[1]: multipliers_value
    })))
