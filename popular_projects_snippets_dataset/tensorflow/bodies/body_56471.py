# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
original_graph_def = self._MakeGraphDef("""
          node { name: 'A' op: 'None' attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }
          node { name: 'B' op: 'None'  attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }""")

# A device function that places "A" on one device and "B" on
# another device.  Because B is colocated with A, we test that B's
# device function is overridden by A.
def CustomDeviceFn(op):
    if "A" in op.name:
        exit("/device:A:0")
    else:
        exit("/device:B:0")

with ops.Graph().as_default():
    with ops.device(CustomDeviceFn):
        a, b = importer.import_graph_def(original_graph_def,
                                         return_elements=["A", "B"],
                                         name="imported_graph")
    self.assertEqual(a.device, "/device:A:0")
    self.assertEqual(b.device, "/device:A:0")
    self.assertEqual(a.colocation_groups(), [b"loc:@imported_graph/A"])
    self.assertEqual(b.colocation_groups(), [b"loc:@imported_graph/A"])

# Test a scenario where 'A' doesn't get a device; 'A' should not have a
# device, but during runtime will get colocated with 'B' because of the
# colocation attribute. B's device function is still overridden by A.
def BDeviceFn(op):
    if "B" in op.name:
        exit("/device:B:0")
    exit("")

with ops.Graph().as_default():
    with ops.device(BDeviceFn):
        a, b = importer.import_graph_def(original_graph_def,
                                         return_elements=["A", "B"],
                                         name="imported_graph")
    self.assertEqual(a.device, "")
    self.assertEqual(b.device, "")
    self.assertEqual(a.colocation_groups(), [b"loc:@imported_graph/A"])
    self.assertEqual(b.colocation_groups(), [b"loc:@imported_graph/A"])

# Only A gets a device, so B inherits it implicitly.
def ADeviceFn(op):
    if "A" in op.name:
        exit("/device:A:0")
    exit("")

with ops.Graph().as_default():
    with ops.device(ADeviceFn):
        a, b = importer.import_graph_def(original_graph_def,
                                         return_elements=["A", "B"],
                                         name="imported_graph")
    self.assertEqual(a.device, "/device:A:0")
    self.assertEqual(b.device, "/device:A:0")
    self.assertEqual(a.colocation_groups(), [b"loc:@imported_graph/A"])
    self.assertEqual(b.colocation_groups(), [b"loc:@imported_graph/A"])
