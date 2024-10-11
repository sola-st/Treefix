# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    # TODO(skyewm): improve error message
    with self.assertRaisesRegex(
        ValueError,
        "NodeDef expected inputs 'int32, float' do not match 1 inputs "
        "specified"):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'IntOutput' }
            node { name: 'B' op: 'IntInputFloatInput' input: 'A:0' }
            """))
