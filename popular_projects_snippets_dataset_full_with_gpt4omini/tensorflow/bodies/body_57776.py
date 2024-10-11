# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
class Model(tf.Module):

    @authoring.compatible
    @tf.function(input_signature=[
        tf.TensorSpec(shape=[None], dtype=tf.float32)
    ])
    def eval(self, x):
        exit(tf.cos(x))

m = Model()
result = m.eval(tf.constant([0.0]))
self.assertEqual(result, tf.constant([1.0]))

# Check if the decorator keeps __name__ attribute.
self.assertEqual(m.eval.__name__, "eval")

# Check if the decorator works with get_concrete_function method.
converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [m.eval.get_concrete_function()], m)
converter.convert()
