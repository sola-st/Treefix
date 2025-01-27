# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        TypeError,
        r"Argument `input_map` must be a dictionary. Obtained list"):
        importer.import_graph_def(
            self._MakeGraphDef(""), input_map=[constant_op.constant(5.0)])
graph_def = self._MakeGraphDef("""
         node { name: 'a' op: 'Placeholder'
                attr { key: 'dtype' value { type: DT_FLOAT } }}
         node { name: 'id' op: 'Identity' input: 'a:0'
                attr { key: 'T' value { type: DT_FLOAT } }}""")
with ops.Graph().as_default():
    with self.assertRaises(ValueError) as e:
        importer.import_graph_def(
            graph_def,
            input_map={"a:0": variables.Variable(5.0)},
            name="")
    self.assertStartsWith(str(e.exception),
                          "tf.import_graph_def() requires a non-empty `name` "
                          "if `input_map` contains non-Tensor values.")
with ops.Graph().as_default():
    t, = importer.import_graph_def(
        graph_def,
        input_map={"a:0": constant_op.constant(5.0)},
        name="",
        return_elements=["id:0"])
    with self.cached_session():
        self.assertEqual(5.0, self.evaluate(t))
