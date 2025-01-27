# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
# TODO(skyewm): improve error message
error_msg = ("Input 0 of node import/B was passed int32 from import/A:0 "
             "incompatible with expected float.")
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError, error_msg):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'IntOutput' }
            node { name: 'B' op: 'FloatInput' input: 'A:0' }
            """))
