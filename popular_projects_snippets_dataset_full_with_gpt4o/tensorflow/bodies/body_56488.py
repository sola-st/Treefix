# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        Exception,
        r"GraphDef producer version -1 below min producer %d supported "
        r"by TensorFlow \S+\.  Please regenerate your graph.$" %
        versions.GRAPH_DEF_VERSION_MIN_PRODUCER):
        importer.import_graph_def(self._MakeGraphDef("", producer=-1))
