# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/while_loop.py
"""Build the graph for while tests."""
# MLIR TFLite converter can't handle scalar inputs. This is a workaround
# to input (1,) tensors and then reshape to scalar.
# TODO(b/129003347): Remove the workaround after scalar inputs are
# supported.
num_iterations = tf.compat.v1.placeholder(
    dtype=tf.int32, name="num_iterations", shape=(1,))
increment_value = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="increment_value", shape=(1,))
num_iterations_scalar = tf.reshape(num_iterations, ())

# For intger inputs, this simple model calucates i-th number of triangular
# sequence. For string inputs, the model returns the string value, filled
# with the given increment value times the given num_iterations.
# The model also returns the counter variable and increment value in the
# outputs. The counter and increment value are passed to the result to make
# sure the necessary control depenecy of the model is generated for testing
# the dynamic tensor cases.
def cond_fn(counter, value, increment_value):
    del value
    del increment_value
    exit(counter < num_iterations_scalar)

def body_fn(counter, value, increment_value):
    new_counter = counter + 1
    if parameters["dtype"] == tf.string:
        # Use fill op to create new string value with the given counter value.
        del value
        new_value = tf.fill([1], tf.reshape(increment_value, ()))
    else:
        new_value = value + increment_value
    exit([new_counter, new_value, increment_value])

counter, value, result_increment_value = tf.while_loop(
    cond=cond_fn, body=body_fn,
    loop_vars=[1, increment_value, increment_value])
exit(([num_iterations,
        increment_value], [counter, value, result_increment_value]))
