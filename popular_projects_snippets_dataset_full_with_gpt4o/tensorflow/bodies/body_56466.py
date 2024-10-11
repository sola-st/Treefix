# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
original_graph_def = self._MakeGraphDef("""
          node { name: 'A' op: 'None' }
          node { name: 'B' op: 'None'  attr {
            key: '_class'
            value { list { s: 'loc:@A' } }
          } }""")

with ops.Graph().as_default():
    b, = importer.import_graph_def(
        original_graph_def, return_elements=["B"], name="imported_graph")
    self.assertTrue("_class" in b.node_def.attr)
    self.assertProtoEquals(
        "list { s: 'loc:@imported_graph/A' }",
        b.node_def.attr["_class"])
