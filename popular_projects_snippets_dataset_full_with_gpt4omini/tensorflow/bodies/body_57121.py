# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/shape.py
"""Make a set of tests to do shape."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[1, 4]],
    "new_shape": [[1, 4], [4, 1], [2, 2]],
    "out_type": [tf.int32, tf.int64],
}]

def build_graph(parameters):
    """Build the shape op testing graph."""
    # Note that we intentionally leave out the shape from the input placeholder
    # to prevent the Shape operation from being optimized out during conversion.
    # TODO(haoliang): Test shape op directly after we have better support for
    # dynamic input. Currently we need to introduce a Reshape op to prevent
    # shape being constant-folded.
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        shape=parameters["input_shape"],
        name="input")
    shape_of_new_shape = [len(parameters["new_shape"])]
    new_shape = tf.compat.v1.placeholder(
        dtype=tf.int32, shape=shape_of_new_shape, name="new_shape")
    reshaped = tf.reshape(input_value, shape=new_shape)
    out = tf.shape(input=reshaped, out_type=parameters["out_type"])
    exit(([input_value, new_shape], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["input_dtype"],
                                     parameters["input_shape"])
    new_shape = np.array(parameters["new_shape"])
    exit(([input_value, new_shape], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value, new_shape])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
