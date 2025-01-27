# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    a, b = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'TwoIntOutputs' }
          node { name: 'B' op: 'IntInput' input: 'A' }
          """),
        return_elements=["A", "B"])

    self.assertEqual(b.inputs[0], a.outputs[0])
