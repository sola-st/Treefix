# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError,
                                "Node 'B': Unknown input node 'A:0'"):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'B' op: 'FloatInput' input: 'A:0' }
            """))
