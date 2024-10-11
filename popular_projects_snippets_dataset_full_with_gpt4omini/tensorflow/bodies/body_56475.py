# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
original_graph_def = self._MakeGraphDef("""
          node { name: 'B' op: 'None'  attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }""")

with ops.Graph().as_default():
    with self.assertRaisesRegex(
        ValueError, "Node 'B' expects to be colocated with unknown node 'A'"):
        importer.import_graph_def(
            original_graph_def, return_elements=["B"], name="imported_graph")
