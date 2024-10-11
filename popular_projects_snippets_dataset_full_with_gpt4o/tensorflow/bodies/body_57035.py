# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/roll.py
"""Make a set of tests to do roll with constant shift and axis."""

def build_graph(parameters):
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    outs = tf.roll(
        input_value, shift=parameters["shift"], axis=parameters["axis"])
    exit(([input_value], [outs]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["input_dtype"],
                                     parameters["input_shape"])
    exit(([input_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
