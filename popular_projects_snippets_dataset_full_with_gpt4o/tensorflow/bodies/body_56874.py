# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fully_connected.py
# pylint: disable=g-doc-return-or-yield, g-doc-args
"""Build list of input values.

    It either contains 1 tensor (input_values1) or
    2 tensors (input_values1, input_values2) based on whether the second input
    is a constant or variable input.
    """

values = [
    create_tensor_data(
        np.float32, shape=parameters["shape1"], min_value=-1, max_value=1)
]
if not parameters["constant_filter"]:
    values.append(
        create_tensor_data(
            np.float32, parameters["shape2"], min_value=-1, max_value=1))
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
