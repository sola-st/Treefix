# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    # Mapping an unused node output should succeed.
    importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'IntOutput' }
          """),
        input_map={"A:0": constant_op.constant(5.0)})

    # Mapping a non-existent output of an existing node should fail.
    with self.assertRaisesRegex(
        ValueError,
        r"Attempted to map inputs that were not found in graph_def: \[A:2\]"):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'IntOutput' }
            """),
            input_map={"A:2": constant_op.constant(5.0)})
