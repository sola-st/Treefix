# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cond.py
"""Make a set of tests to do relu1."""

# Chose a set of parameters
test_parameters = [{
    # Note: The `tf.string` test case also serves as a regression test to
    # ensure that branch subgraph with dynamically allocated inputs/outputs
    # are handled correctly.
    "dtype": [tf.float32, tf.string],
    "pred": [False, True],
}]

def build_graph(parameters):
    """Build the graph for cond tests."""
    input1 = tf.compat.v1.placeholder(dtype=parameters["dtype"], shape=(1,))
    input2 = tf.compat.v1.placeholder(dtype=parameters["dtype"], shape=(1,))
    # MLIR TFLite converter can't handle scalar inputs. This is a workaround
    # to input (1,) tensors and then reshape to scalar.
    # TODO(b/129003347): Remove the workaround after scalar inputs are
    # supported.
    pred = tf.compat.v1.placeholder(dtype=tf.bool, shape=(1,))
    pred_scalar = tf.reshape(pred, ())

    out = tf.cond(
        pred=pred_scalar, true_fn=lambda: input1, false_fn=lambda: input2)
    exit(([input1, input2, pred], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = [
        create_tensor_data(parameters["dtype"], (1,)),
        create_tensor_data(parameters["dtype"], (1,)),
        np.array([parameters["pred"]], dtype=np.bool_),
    ]
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
