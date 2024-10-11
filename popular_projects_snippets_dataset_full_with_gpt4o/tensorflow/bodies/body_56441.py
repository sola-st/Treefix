# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    a, b, c, d = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'RefOutput' }
          node { name: 'B' op: 'IntOutput' }
          node { name: 'C' op: 'TwoIntInputs' input: 'A:0' input: 'B:0' }
          node { name: 'D' op: 'RefInputIntInput' input: 'A:0' input: 'B:0' }
          """),
        return_elements=["A", "B", "C", "D"])

    self.assertEqual(c.inputs[0], a.outputs[0])
    self.assertEqual(c.inputs[1], b.outputs[0])
    self.assertEqual(d.inputs[0], a.outputs[0])
    self.assertEqual(d.inputs[1], b.outputs[0])

    self.assertEqual(a.outputs[0].dtype, dtypes.int32_ref)
    self.assertEqual(c._input_types, [dtypes.int32, dtypes.int32])
    self.assertEqual(c.outputs, [])
    self.assertEqual(d._input_types, [dtypes.int32_ref, dtypes.int32])
    self.assertEqual(d.outputs, [])
