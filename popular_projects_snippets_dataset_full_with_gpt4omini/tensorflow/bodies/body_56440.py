# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    a, b = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'None' }
          node { name: 'B' op: 'None' input: '^A' }
          """),
        return_elements=["A", "B"])

    self.assertEqual(b.control_inputs, [a])
