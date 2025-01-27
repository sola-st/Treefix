# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    a, = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'None' }
          """),
        return_elements=["A"],
        name=None)
    self.assertEqual(a.name, "import/A")
