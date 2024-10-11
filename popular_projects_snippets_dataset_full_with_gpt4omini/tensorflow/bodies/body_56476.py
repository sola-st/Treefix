# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default() as g:
    init_version = g.version
    importer.import_graph_def(self._MakeGraphDef(""))
    self.assertEqual(init_version, g.version)
