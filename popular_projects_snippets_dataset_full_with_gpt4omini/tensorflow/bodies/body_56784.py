# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/binary_op.py
"""Builds operand inputs for op."""
input_shape_1 = populate_dynamic_shape(parameters,
                                       parameters["input_shape_1"])
input_shape_2 = populate_dynamic_shape(parameters,
                                       parameters["input_shape_2"])
if allow_fully_quantize:
    input1 = create_tensor_data(
        parameters["dtype"], input_shape_1, min_value=-1, max_value=1)
    input2 = create_tensor_data(
        parameters["dtype"], input_shape_2, min_value=-1, max_value=1)
else:
    input1 = create_tensor_data(parameters["dtype"], input_shape_1)
    input2 = create_tensor_data(parameters["dtype"], input_shape_2)
exit(([input1, input2], sess.run(
    outputs, feed_dict={
        inputs[0]: input1,
        inputs[1]: input2
    })))
