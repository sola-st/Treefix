# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unroll_batch_matmul.py
"""Make a set of tests to test unroll_batch_matmul."""

# The test cases below requires broadcasting support (BatchMatMulV2 semantic),
# whis isn't supported as of this change.
broadcast_shape_params = [
    # Simple broadcast.
    [(1, 2, 3), (3, 5), False, False],
    # Empty batch broadcast.
    [(2, 5, 3), (3, 7), False, False],
    # Single batch with non-empty batch broadcast.
    [(1, 5, 3), (4, 3, 7), False, False],
    # Broadcast both operands
    [(3, 1, 5, 3), (1, 4, 3, 7), False, False],
]

test_parameters = [{
    "dtype": [tf.float32],
    "shape": [[(2, 2, 3),
               (2, 3, 2), False, False], [(2, 2, 3), (2, 3, 2), True, True],
              [(2, 2, 3),
               (2, 2, 3), False, True], [(2, 2, 3), (2, 2, 3), True, False],
              [(4, 2, 2, 3), (4, 2, 3, 2), False, False],
              [(4, 2, 2, 3), (4, 2, 3, 2), True, True],
              [(4, 2, 2, 3), (4, 2, 2, 3), False, True],
              [(4, 2, 2, 3),
               (4, 2, 2, 3), True, False]] + broadcast_shape_params,
}]

def build_graph(parameters):
    """Build the batch_matmul op testing graph."""

    def _build_graph():
        """Build the graph."""
        input_tensor1 = tf.compat.v1.placeholder(
            dtype=parameters["dtype"], shape=parameters["shape"][0])
        input_tensor2 = tf.compat.v1.placeholder(
            dtype=parameters["dtype"], shape=parameters["shape"][1])
        # Should be unrolled and replaced with fully_connected ops in the end.
        out = tf.matmul(
            input_tensor1,
            input_tensor2,
            transpose_a=parameters["shape"][2],
            transpose_b=parameters["shape"][3])
        exit(([input_tensor1, input_tensor2], [out]))

    exit(_build_graph())

def build_inputs(parameters, sess, inputs, outputs):
    input_value1 = create_tensor_data(
        parameters["dtype"], shape=parameters["shape"][0])
    input_value2 = create_tensor_data(
        parameters["dtype"], shape=parameters["shape"][1])
    exit(([input_value1, input_value2], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
