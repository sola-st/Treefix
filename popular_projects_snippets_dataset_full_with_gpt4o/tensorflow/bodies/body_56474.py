# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
original_graph_def = self._MakeGraphDef("""
          node { name: 'A' op: 'None' }
          node { name: 'B' op: 'None'  attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }""")

with ops.Graph().as_default():
    a, b = importer.import_graph_def(
        original_graph_def, return_elements=["A", "B"], name="")
    a_1, b_1 = importer.import_graph_def(
        original_graph_def, return_elements=["A", "B"], name="")

    self.assertEqual(a.name, "A")
    self.assertEqual(b.name, "B")
    self.assertEqual(b.colocation_groups(), [b"loc:@A"])

    self.assertEqual(a_1.name, "A_1")
    self.assertEqual(b_1.name, "B_1")
    self.assertEqual(b_1.colocation_groups(), [b"loc:@A_1"])
