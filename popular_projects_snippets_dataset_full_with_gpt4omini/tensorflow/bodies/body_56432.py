# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    a, b, c, d = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'IntOutputFloatOutput' }
          node { name: 'B' op: 'ListOutput'
                 attr { key: 'T'
                        value { list { type: DT_INT32 type: DT_FLOAT } } } }
          node { name: 'C' op: 'ListInput'
                 attr { key: 'N' value { i: 2 } }
                 attr { key: 'T' value { type: DT_INT32 } }
                 input: 'A:0' input: 'B:0' }
          node { name: 'D' op: 'ListInput'
                 attr { key: 'N' value { i: 2 } }
                 attr { key: 'T' value { type: DT_FLOAT } }
                 input: 'A:1' input: 'B:1' }
          """),
        return_elements=["A", "B", "C", "D"],
        name="import")

    # Assert that the import process creates distinct tensors.
    self.assertNotEqual(a.outputs[0].name, a.outputs[1].name)
    self.assertNotEqual(b.outputs[0].name, b.outputs[1].name)
    self.assertNotEqual(a.outputs[0].name, b.outputs[0].name)
    self.assertNotEqual(a.outputs[0].name, b.outputs[1].name)
    self.assertNotEqual(a.outputs[1].name, b.outputs[0].name)
    self.assertNotEqual(a.outputs[1].name, b.outputs[1].name)

    # Assert that the ops are connected according to the GraphDef topology.
    self.assertEqual(c.inputs[0], a.outputs[0])
    self.assertEqual(c.inputs[1], b.outputs[0])
    self.assertEqual(d.inputs[0], a.outputs[1])
    self.assertEqual(d.inputs[1], b.outputs[1])

    # Check the types of the returned ops and tensors.
    self.assertEqual(a.type, "IntOutputFloatOutput")
    self.assertEqual(b.type, "ListOutput")
    self.assertEqual(c.type, "ListInput")
    self.assertEqual(d.type, "ListInput")
    self.assertEqual(a.outputs[0].dtype, dtypes.int32)
    self.assertEqual(a.outputs[1].dtype, dtypes.float32)
    self.assertEqual(b.outputs[0].dtype, dtypes.int32)
    self.assertEqual(b.outputs[1].dtype, dtypes.float32)

    # Check the names of the returned ops.
    self.assertEqual(a.name, "import/A")
    self.assertEqual(b.name, "import/B")
    self.assertEqual(c.name, "import/C")
    self.assertEqual(d.name, "import/D")

    # Check that the op_def is still available.
    self.assertNotEqual(None, a.op_def)
