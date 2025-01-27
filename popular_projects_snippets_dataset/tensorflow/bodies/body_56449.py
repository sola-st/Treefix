# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
# L2 loss produces a scalar shape, but the graph
# has the wrong shape, so raise an error.
with ops.Graph().as_default():
    with self.assertRaises(ValueError) as e:
        _ = importer.import_graph_def(
            self._MakeGraphDef("""
              node { name: 'A' op: 'FloatOutput' }
              node { name: 'B' op: 'L2Loss'
                     input: 'A:0'
                     attr { key: 'T' value { type: DT_FLOAT } }
                     attr { key: '_output_shapes'
                            value { list { shape { dim { size: 43 } } } } } }
            """),
            return_elements=["B"],
            name="import")
        self.assertTrue(
            "Shapes () and (43,) are not compatible" in str(e.exception))
