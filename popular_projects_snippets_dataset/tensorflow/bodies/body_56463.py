# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default() as g:
    ret = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'None' }
          """))
    self.assertEqual(ret, None)

    a = g.get_operation_by_name("import/A")
    self.assertEqual(a.type, "None")
