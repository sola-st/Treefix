# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        ValueError,
        r"Invalid return output 1 of node 'A', which has 1 output\(s\)"):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'IntOutput' }
            """),
            return_elements=["A:1"])

    with self.assertRaisesRegex(
        ValueError, "Requested return tensor 'B:0' not found in graph def"):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'IntOutput' }
            """),
            return_elements=["B:0"])

    with self.assertRaisesRegex(ValueError,
                                "Cannot convert 'A:B:0' to a tensor name."):
        importer.import_graph_def(
            self._MakeGraphDef("""
            node { name: 'A' op: 'IntOutput' }
            """),
            return_elements=["A:B:0"])
