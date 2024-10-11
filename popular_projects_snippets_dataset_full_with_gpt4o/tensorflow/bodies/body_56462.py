# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        ValueError, "Input 0 of node import/B was passed float from Const:0 "
        "incompatible with expected int32."):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'IntOutput' }
            node { name: 'B' op: 'IntInput' input: 'A:0' }
            """),
            input_map={"A:0": constant_op.constant(5.0)})
