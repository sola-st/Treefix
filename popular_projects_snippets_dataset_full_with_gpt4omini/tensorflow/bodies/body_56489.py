# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        ValueError,
        r"GraphDef min consumer version %d above current version %d "
        r"for TensorFlow \S+\.  Please upgrade TensorFlow\.$" %
        (1 << 30, versions.GRAPH_DEF_VERSION)):
        importer.import_graph_def(self._MakeGraphDef("", min_consumer=1 << 30))
