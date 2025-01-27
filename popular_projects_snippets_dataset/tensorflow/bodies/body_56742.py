# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/depthwiseconv.py
# pylint: disable=g-doc-return-or-yield, g-doc-args
"""Build list of input values.

    It either contains 1 tensor (input) or 2 tensors (input, filter) based on
    whether filter is constant or variable input.
    """

input_shape, filter_shape = get_tensor_shapes(parameters)
values = [
    create_tensor_data(np.float32, input_shape, min_value=-1, max_value=1)
]
if not parameters["constant_filter"]:
    values.append(
        create_tensor_data(
            np.float32, filter_shape, min_value=-1, max_value=1))
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
