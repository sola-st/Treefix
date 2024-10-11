# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default():
    # Create name scope but don't create any ops with it
    with ops.name_scope("foo"):
        pass

    # Import graph def that uses name scope name
    op, = importer.import_graph_def(
        self._MakeGraphDef("node { name: 'foo' op: 'IntOutput' }"),
        return_elements=["foo"],
        name="")

    self.assertEqual(op.name, "foo")
