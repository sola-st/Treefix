# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
original_graph_def = self._MakeGraphDef("""
          node { name: 'A' op: 'None'}
          node { name: 'B' op: 'None'}
          node { name: 'C' op: 'None'  attr {
            key: '_class'
            value { list { s: 'loc:@A' s: 'loc:@B' } }
          } }""")

# A device function that places "B" on a device, and "A" is empty.
#
# B and C should contain "/device:B".  A will not right now.  But
# because of the colocation property, at runtime it would be
# placed with B and C.
def CustomDeviceFn(op):
    if "B" in op.name:
        exit("/device:B:0")
    exit("")

with ops.Graph().as_default():
    with ops.device(CustomDeviceFn):
        a, b, c = importer.import_graph_def(original_graph_def,
                                            return_elements=["A", "B", "C"],
                                            name="imported_graph")
    self.assertEqual(a.device, "")
    self.assertEqual(b.device, "/device:B:0")
    self.assertEqual(c.device, "/device:B:0")
    self.assertEqual(a.colocation_groups(), [b"loc:@imported_graph/A"])
    self.assertEqual(b.colocation_groups(), [b"loc:@imported_graph/B"])
    self.assertEqual(c.colocation_groups(),
                     [b"loc:@imported_graph/A", b"loc:@imported_graph/B"])
