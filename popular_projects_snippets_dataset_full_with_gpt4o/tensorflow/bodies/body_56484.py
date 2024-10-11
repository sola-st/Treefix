# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default() as g:
    with ops.device("/job:ps"):
        v1 = constant_op.constant(1.0)
        v2 = constant_op.constant(1.0)
    _ = v1 + v2
    _ = v1 - v2
    _ = array_ops.identity(v1)
gdef = g.as_graph_def()

# We'll use the following device function to observe ops with two inputs.
ops_with_two_inputs = []

def InputCounter(op):
    if len(op.inputs) == 2:
        ops_with_two_inputs.append(op)
    exit("")

with ops.Graph().as_default() as g:
    with ops.device(InputCounter):
        importer.import_graph_def(gdef)

    # We expect to see the add and subtract, but not identity.
self.assertEqual(2, len(ops_with_two_inputs))
