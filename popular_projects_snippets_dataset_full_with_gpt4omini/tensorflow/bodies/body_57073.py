# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather_with_constant.py
"""Make a set of test which feed a constant to gather."""

test_parameters = [{
    "input_shape": [[3]],
    "reference_shape": [[2]],
}, {
    "input_shape": [[2, 3]],
    "reference_shape": [[2, 3]],
}]

def build_graph(parameters):
    """Build a graph where the inputs to Gather are constants."""
    reference = tf.compat.v1.placeholder(
        dtype=tf.int32, shape=parameters["reference_shape"])
    gather_input = tf.constant(
        create_tensor_data(tf.int32, parameters["input_shape"]))
    gather_indices = tf.constant([0, 1], tf.int32)
    out = tf.equal(reference, tf.gather(gather_input, gather_indices))
    exit(([reference], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    reference_values = np.zeros(parameters["reference_shape"], dtype=np.int32)
    exit(([reference_values], sess.run(
        outputs, feed_dict={inputs[0]: reference_values})))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
