# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/parse_example.py
"""Make a set of tests to use parse_example."""

# Chose a set of parameters
test_parameters = [{
    "feature_dtype": [tf.string, tf.float32, tf.int64],
    "is_dense": [True, False],
    "feature_shape": [[1], [2], [16]],
}]

def build_graph(parameters):
    """Build the graph for parse_example tests."""
    feature_dtype = parameters["feature_dtype"]
    feature_shape = parameters["feature_shape"]
    is_dense = parameters["is_dense"]
    input_value = tf.compat.v1.placeholder(
        dtype=tf.string, name="input", shape=[1])
    if is_dense:
        feature_default_value = np.zeros(shape=feature_shape)
        if feature_dtype == tf.string:
            feature_default_value = np.array(["missing"] * feature_shape[0])
        features = {
            "x":
                tf.io.FixedLenFeature(
                    shape=feature_shape,
                    dtype=feature_dtype,
                    default_value=feature_default_value)
        }
    else:  # Sparse
        features = {"x": tf.io.VarLenFeature(dtype=feature_dtype)}
    out = tf.io.parse_example(serialized=input_value, features=features)
    output_tensor = out["x"]
    if not is_dense:
        output_tensor = out["x"].values
    exit(([input_value], [output_tensor]))

def build_inputs(parameters, sess, inputs, outputs):
    feature_dtype = parameters["feature_dtype"]
    feature_shape = parameters["feature_shape"]
    input_values = [create_example_data(feature_dtype, feature_shape)]
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

extra_convert_options = ExtraConvertOptions()
extra_convert_options.allow_custom_ops = True
make_zip_of_tests(options, test_parameters, build_graph, build_inputs,
                  extra_convert_options)
