# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tensor_list_concat.py
"""Make a set of tests to do TensorListConcatV2."""

test_parameters = [
    {
        "element_dtype": [tf.float32, tf.int32],
        "num_elements": [4, 5, 6],
        "element_shape": [[5], [3, 3]],
    },
]

def build_graph(parameters):
    """Build the TensorListConcatV2 op testing graph."""
    data = tf.compat.v1.placeholder(
        dtype=parameters["element_dtype"],
        shape=[parameters["num_elements"]] + parameters["element_shape"])
    tensor_list = list_ops.tensor_list_from_tensor(data,
                                                   parameters["element_shape"])
    out = list_ops.tensor_list_concat(tensor_list, parameters["element_dtype"],
                                      parameters["element_shape"])
    exit(([data], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    data = create_tensor_data(parameters["element_dtype"],
                              [parameters["num_elements"]] +
                              parameters["element_shape"])
    exit(([data], sess.run(outputs, feed_dict=dict(zip(inputs, [data])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
