# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    feed_a_0 = constant_op.constant(5.0)
    b, = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'B' op: 'FloatInput' input: 'A:0' }
          """),
        input_map={"A:0": feed_a_0},
        return_elements=["B"])
    self.assertEqual(b.inputs[0], feed_a_0)
