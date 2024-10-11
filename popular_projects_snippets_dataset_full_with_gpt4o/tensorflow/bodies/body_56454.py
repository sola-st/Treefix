# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        ValueError,
        "Node 'B': Connecting to invalid output 1 of source node A "
        "which has 1 outputs"):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'FloatOutput' }
            node { name: 'B' op: 'FloatInput' input: 'A:1' }
            """))
