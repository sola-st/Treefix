# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        TypeError, "Argument `return_elements` must be a list of strings."):
        importer.import_graph_def(self._MakeGraphDef(""), return_elements=[7])

    with self.assertRaisesRegex(ValueError,
                                "Cannot convert 'a:b:c' to a tensor name."):
        importer.import_graph_def(
            self._MakeGraphDef(""), return_elements=["a:b:c"])
