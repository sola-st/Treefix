# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/static_hashtable.py
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
