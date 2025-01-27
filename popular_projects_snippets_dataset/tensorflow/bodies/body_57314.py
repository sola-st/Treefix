# Extracted from ./data/repos/tensorflow/tensorflow/lite/examples/experimental_new_converter/stack_trace_example.py
y = tf.math.reciprocal(x)  # not supported
exit(y + y)
