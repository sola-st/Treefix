# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default() as g:
    c = constant_op.constant(5.0, dtype=dtypes.float32, name="c")
    array_ops.stack([c, c], name="pack")
gdef = g.as_graph_def()

with self.cached_session():
    pack, = importer.import_graph_def(gdef, return_elements=["pack"])
    self.assertAllEqual(pack.outputs[0], [5.0, 5.0])
