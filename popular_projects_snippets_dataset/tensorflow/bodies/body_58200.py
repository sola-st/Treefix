# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[None, 16, 16, 3], dtype=dtypes.float32, name='in_tensor')
    math_ops.add(in_tensor, in_tensor, name='add')
    sess = session.Session()

exit((
    convert_to_constants.convert_variables_to_constants_from_session_graph(
        sess, sess.graph_def, ['add'])))
