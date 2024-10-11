# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a partial shape overriding case via the constructor."""
with ops.Graph().as_default():
    in_tensor_a = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32, name='in_tensor_a')
    in_tensor_b = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32, name='in_tensor_b')
    math_ops.add(in_tensor_a, in_tensor_b, name='add')
    sess = session.Session()

frozen_graph_def = (
    convert_to_constants.convert_variables_to_constants_from_session_graph(
        sess, sess.graph_def, ['add']))

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter(frozen_graph_def, None, None,
                                 [('in_tensor_a', [2, 16, 16, 3])], ['add'])
# There is an unhandled Placeholder op.
with self.assertRaises(ConverterError):
    converter.convert()
