# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a concrete function has debug info captured."""
root = autotrackable.AutoTrackable()
root.v1 = tf.Variable(3.)
root.f = tf.function(lambda x: root.v1 * x)
input_data = tf.constant(1., shape=[1])
concrete_func = root.f.get_concrete_function(input_data)

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
converter.convert()
self._assertValidDebugInfo(converter._debug_info)
