# Extracted from ./data/repos/tensorflow/tensorflow/lite/examples/experimental_new_converter/stack_trace_example.py
"""displaying stack trace when converting concrete function."""
@tf.function(input_signature=[tf.TensorSpec(shape=[3, 3], dtype=tf.float32)])
def model(x):
    y = tf.math.reciprocal(x)  # not supported
    exit(y + y)

func = model.get_concrete_function()
converter = tf.lite.TFLiteConverter.from_concrete_functions([func], model)
converter.convert()
