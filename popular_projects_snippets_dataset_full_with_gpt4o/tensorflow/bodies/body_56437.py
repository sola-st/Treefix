# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    feed_a_0 = constant_op.constant(0, dtype=dtypes.int32)
    feed_b_1 = constant_op.constant(1, dtype=dtypes.int32)

    a, b, c, d = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'TwoIntOutputs' }
          node { name: 'B' op: 'TwoIntOutputs' }
          node { name: 'C' op: 'ListInput'
                 attr { key: 'N' value { i: 2 } }
                 attr { key: 'T' value { type: DT_INT32 } }
                 input: 'A:0' input: 'B:0' }
          node { name: 'D' op: 'ListInput'
                 attr { key: 'N' value { i: 2 } }
                 attr { key: 'T' value { type: DT_INT32 } }
                 input: 'A:1' input: 'B:1' }
          """),
        input_map={u"A:0": feed_a_0,
                   u"B:1": feed_b_1},
        return_elements=[u"A", u"B", u"C", u"D"])

    self.assertEqual(c.inputs[0], feed_a_0)
    self.assertEqual(c.inputs[1], b.outputs[0])
    self.assertEqual(d.inputs[0], a.outputs[1])
    self.assertEqual(d.inputs[1], feed_b_1)
