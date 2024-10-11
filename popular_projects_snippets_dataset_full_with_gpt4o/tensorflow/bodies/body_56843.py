# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/strided_slice.py
"""Utility function to make strided_slice_tests based on parameters."""

def build_graph(parameters):
    """Build graph for stride_slice test."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    if parameters["constant_indices"]:
        begin = parameters["begin"]
        end = parameters["end"]
        strides = parameters["strides"]
        tensors = [input_tensor]
    else:
        begin = tf.compat.v1.placeholder(
            dtype=parameters["index_type"],
            name="begin",
            shape=[len(parameters["begin"])])
        end = tf.compat.v1.placeholder(
            dtype=parameters["index_type"],
            name="end",
            shape=[len(parameters["end"])])
        strides = None
        if parameters["strides"] is not None:
            strides = tf.compat.v1.placeholder(
                dtype=parameters["index_type"],
                name="strides",
                shape=[len(parameters["strides"])])
        tensors = [input_tensor, begin, end]
        if strides is not None:
            tensors.append(strides)

    kwargs = {}
    if parameters.get("ellipsis_mask", None):
        kwargs.update({"ellipsis_mask": parameters["ellipsis_mask"]})
    if parameters.get("new_axis_mask", None):
        kwargs.update({"new_axis_mask": parameters["new_axis_mask"]})

    out = tf.strided_slice(
        input_tensor,
        begin,
        end,
        strides,
        begin_mask=parameters["begin_mask"],
        end_mask=parameters["end_mask"],
        shrink_axis_mask=parameters["shrink_axis_mask"],
        **kwargs)
    exit((tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Build inputs for stride_slice test."""
    input_values = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
    index_type = MAP_TF_TO_NUMPY_TYPE[parameters["index_type"]]
    values = [input_values]
    if not parameters["constant_indices"]:
        begin_values = np.array(parameters["begin"]).astype(index_type)
        end_values = np.array(parameters["end"]).astype(index_type)
        stride_values = (
            np.array(parameters["strides"]).astype(index_type)
            if parameters["strides"] is not None else None)
        values.append(begin_values)
        values.append(end_values)
        if stride_values is not None:
            values.append(stride_values)

    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=expected_tf_failures)
