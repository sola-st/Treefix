# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/static_hashtable.py
"""Make a set of tests to use static hashtable."""

# Chose a set of parameters
test_parameters = [{
    "table": [(tf.string, tf.int64, ["1", "2", "3"], [4, 5, 6], -1),
              (tf.int64, tf.string, [1, 2, 3], ["4", "5", "6"], "-1")],
    "input_shape": [[], [3], [1], [10]],
}]

def build_graph(parameters):
    """Build the graph for static hashtable tests."""
    (key_dtype, value_dtype, keys, values, default_value) = parameters["table"]

    key_tensor = tf.constant(keys, dtype=key_dtype)
    value_tensor = tf.constant(values, dtype=value_dtype)

    initializer = tf.lookup.KeyValueTensorInitializer(key_tensor, value_tensor)
    table = tf.lookup.StaticHashTable(initializer, default_value)

    with tf.control_dependencies(
        [tf.compat.v1.initializers.tables_initializer()]):
        input_value = tf.compat.v1.placeholder(
            dtype=key_dtype, name="input", shape=parameters["input_shape"])
        out = table.lookup(key_tensor)
    exit(([input_value], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    (key_dtype, _, _, _, _) = parameters["table"]
    input_values = [create_tensor_data(key_dtype, parameters["input_shape"])]
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

extra_convert_options = ExtraConvertOptions()
make_zip_of_tests(options, test_parameters, build_graph, build_inputs,
                  extra_convert_options)
