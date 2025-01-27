# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
time.sleep(random.random() * 0.1)
# Do some graph construction. Try to exercise non-trivial paths.
graph = ops.get_default_graph()
gdef = None
for _ in range(10):
    x = array_ops.placeholder(dtype=dtypes.float32)
    with ops.colocate_with(x):
        y = array_ops.placeholder(dtype=dtypes.float32)
    with ops.device('/cpu:0'):
        z = control_flow_ops.while_loop(
            lambda x, y: x < 10, lambda x, y: (x + 1, x * y), [x, y])
    with graph._attr_scope({'_a': attr_value_pb2.AttrValue(b=False)}):
        gradients_impl.gradients(z, [x, y])
        if gdef is None:
            gdef = graph.as_graph_def()
        else:
            importer.import_graph_def(gdef, name='import')
