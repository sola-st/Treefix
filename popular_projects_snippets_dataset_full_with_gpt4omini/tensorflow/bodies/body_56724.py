# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/while_loop.py
new_counter = counter + 1
if parameters["dtype"] == tf.string:
    # Use fill op to create new string value with the given counter value.
    del value
    new_value = tf.fill([1], tf.reshape(increment_value, ()))
else:
    new_value = value + increment_value
exit([new_counter, new_value, increment_value])
