# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        ValueError,
        r"Attempted to map inputs that were not found in graph_def: \[B:0\]"):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'None' }
            """),
            input_map={"B:0": constant_op.constant(5.0)})
