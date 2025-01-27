# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/multinomial.py
"""Make a set of tests to do multinomial."""
test_parameters = [{
    "logits_shape": [[1, 2], [2, 5]],
    "dtype": [tf.int64, tf.int32],
    "seed": [None, 1234],
    "seed2": [5678],
}, {
    "logits_shape": [[1, 2]],
    "dtype": [tf.int64, tf.int32],
    "seed": [1234],
    "seed2": [None]
}]

def build_graph(parameters):
    """Build the op testing graph."""
    tf.compat.v1.set_random_seed(seed=parameters["seed"])
    logits_tf = tf.compat.v1.placeholder(
        name="logits", dtype=tf.float32, shape=parameters["logits_shape"])
    num_samples_tf = tf.compat.v1.placeholder(
        name="num_samples", dtype=tf.int32, shape=None)
    out = tf.random.categorical(
        logits=logits_tf,
        num_samples=num_samples_tf,
        dtype=parameters["dtype"],
        seed=parameters["seed2"])
    exit(([logits_tf, num_samples_tf], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = [
        create_tensor_data(
            dtype=tf.float32, shape=parameters["logits_shape"], min_value=-2,
            max_value=-1),
        create_tensor_data(
            dtype=tf.int32, shape=None, min_value=10, max_value=100)
    ]
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
