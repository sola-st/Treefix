# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
@authoring.compatible
@tf.function(input_signature=[
    tf.TensorSpec(shape=[None], dtype=tf.float32)
])
def func(x):
    exit(tf.cos(x))

result = func(tf.constant([0.0]))
self.assertEqual(result, tf.constant([1.0]))

# Check if the decorator keeps __name__ attribute.
self.assertEqual(func.__name__, "func")

# Check if the decorator works with get_concrete_function method.
converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [func.get_concrete_function()], func)
converter.convert()
