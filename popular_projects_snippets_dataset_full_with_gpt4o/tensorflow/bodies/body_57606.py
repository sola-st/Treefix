# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test if the warning message when there are redundant arguments."""
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32, name='in_tensor')
    out_tensor = math_ops.add(in_tensor, in_tensor, name='add')
    sess = session.Session()

frozen_graph_def = (
    convert_to_constants.convert_variables_to_constants_from_session_graph(
        sess, sess.graph_def, ['add']))

# Convert model and ensure model is not None.
log = io.StringIO()
handler = logging.StreamHandler(log)
logging.root.addHandler(handler)
converter = lite.TFLiteConverter(frozen_graph_def, [in_tensor],
                                 [out_tensor],
                                 [('in_tensor', [2, 16, 16, 3])], ['add'])

input_warning_message = 'input_arrays_with_shape will be ignored'
output_warning_message = 'output_arrays will be ignored'

# Convert model and ensure model is not None.
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)
self.assertIn(input_warning_message, log.getvalue())
self.assertIn(output_warning_message, log.getvalue())
logging.root.removeHandler(handler)
