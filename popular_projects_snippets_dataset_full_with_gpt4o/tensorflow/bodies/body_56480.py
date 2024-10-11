# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with self.assertRaisesRegex(ValueError, "Node 'A' is not unique"):
    importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'IntOutput' }
          node { name: 'B' op: 'IntOutput' }
          node { name: 'A' op: 'IntOutput' }
          """))
