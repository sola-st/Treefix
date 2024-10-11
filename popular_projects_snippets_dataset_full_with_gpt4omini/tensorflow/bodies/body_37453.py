# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
def summary_op_fn():
    summary_ops.graph('hello')

with self.assertRaisesRegex(
    ValueError,
    r'\'graph_data\' is not tf.Graph or tf.compat.v1.GraphDef',
):
    self.exec_summary_op(summary_op_fn)
