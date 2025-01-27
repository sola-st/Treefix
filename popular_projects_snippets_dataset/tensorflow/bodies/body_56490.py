# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
"""These tests rely on shape fns in test_ops.cc."""
with ops.Graph().as_default():
    importer.import_graph_def(
        self._MakeGraphDef(
            "node { name: 'A' op: 'RequiresOlderGraphVersion' }",
            producer=versions.GRAPH_DEF_VERSION - 1),
        return_elements=["A"])

with ops.Graph().as_default():
    with self.assertRaisesWithPredicateMatch(ValueError,
                                             "Wrong graph version.*"):
        importer.import_graph_def(
            self._MakeGraphDef(
                "node { name: 'A' op: 'RequiresOlderGraphVersion' }",
                producer=versions.GRAPH_DEF_VERSION),
            return_elements=["A"])
