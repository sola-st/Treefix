# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        TypeError, r"Argument `graph_def` must be a GraphDef proto."):
        importer.import_graph_def("")
