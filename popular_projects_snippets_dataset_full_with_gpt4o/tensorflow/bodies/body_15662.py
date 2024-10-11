# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_placeholder_op_test.py
if context.executing_eagerly():
    exit()
graph = ops.Graph()
with graph.as_default():
    ragged_factory_ops.placeholder(
        dtypes.float32, ragged_rank=1, value_shape=[])
    self.assertEqual([op.type for op in graph.get_operations()],
                     ['Placeholder', 'Placeholder'])
