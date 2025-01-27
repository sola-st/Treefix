# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    a = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'OpWithDefaultAttr' }
          """),
        return_elements=["A"])
    self.assertEqual(123.0, a[0].get_attr("default_float"))
