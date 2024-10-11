# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sigmoid_grad.py
"""Make a set of tests to examine sigmoid grad op."""

test_parameters = [{
    "dtype": [tf.float32],
    "input_shape": [[3, 2, 1], [1, 2, 3, 4]],
    "input_range": [(-32, 32)],
}]

def build_graph(parameters):
    y = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], name="y", shape=parameters["input_shape"])
    dy = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], name="dy", shape=parameters["input_shape"])
    out = tf.raw_ops.SigmoidGrad(y=y, dy=dy)
    exit(([y, dy], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    # input is y which is sigmoid(x), hence it's range is between 0 to 1
    y = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=0,
        max_value=1)
    min_value, max_value = parameters["input_range"]
    dy = create_tensor_data(parameters["dtype"], parameters["input_shape"],
                            min_value, max_value)
    values = [y, dy]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
