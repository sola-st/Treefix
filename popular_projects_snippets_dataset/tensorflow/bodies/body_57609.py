# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test an invalid shape overriding case via the constructor."""
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32, name='in_tensor')
    math_ops.add(in_tensor, in_tensor, name='add')
    sess = session.Session()

frozen_graph_def = (
    convert_to_constants.convert_variables_to_constants_from_session_graph(
        sess, sess.graph_def, ['add']))

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter(frozen_graph_def, None, None,
                                 [('wrong_tensor', [2, 16, 16, 3])],
                                 ['add'])
with self.assertRaises(ConverterError):
    converter.convert()
