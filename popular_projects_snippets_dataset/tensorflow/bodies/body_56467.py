# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
# A and B are colocated, device set on A.
original_graph_def = self._MakeGraphDef("""
          node { name: 'A' op: 'None' device: '/device:CPU:0' attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }
          node { name: 'B' op: 'None'  attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }""")

with ops.Graph().as_default():
    a, b = importer.import_graph_def(original_graph_def,
                                     return_elements=["A", "B"],
                                     name="")
    self.assertEqual(a.device, "/device:CPU:0")
    self.assertEqual(b.device, "/device:CPU:0")
    self.assertEqual(a.colocation_groups(), [b"loc:@A"])
    self.assertEqual(b.colocation_groups(), [b"loc:@A"])

# A and B are colocated, device set on B.
original_graph_def = self._MakeGraphDef("""
          node { name: 'A' op: 'None' attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }
          node { name: 'B' op: 'None' device: '/device:CPU:0' attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }""")

with ops.Graph().as_default():
    a, b = importer.import_graph_def(original_graph_def,
                                     return_elements=["A", "B"],
                                     name="")
    # TODO(skyewm): this behavior seems inconsistent with the above. Why is
    # B's device ignored?
    self.assertEqual(a.device, "")
    self.assertEqual(b.device, "")
    self.assertEqual(a.colocation_groups(), [b"loc:@A"])
    self.assertEqual(b.colocation_groups(), [b"loc:@A"])
