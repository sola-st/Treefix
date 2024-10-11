# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/shape_to_strided_slice.py
"""Utility function to make shape_to_strided_slice_tests."""

def build_graph(parameters):
    """Build graph for shape_stride_slice test."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["dynamic_input_shape"])
    begin = parameters["begin"]
    end = parameters["end"]
    strides = parameters["strides"]
    tensors = [input_tensor]
    out = tf.strided_slice(
        tf.shape(input=input_tensor),
        begin,
        end,
        strides,
        begin_mask=parameters["begin_mask"],
        end_mask=parameters["end_mask"])
    exit((tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Build inputs for stride_slice test."""
    input_values = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
    values = [input_values]

    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=expected_tf_failures)
