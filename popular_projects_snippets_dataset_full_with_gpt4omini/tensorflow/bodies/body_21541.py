# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("binary_and_text")
filename = os.path.join(test_dir, "metafile")
# train.Saver is V1 only API.
with ops_lib.Graph().as_default(), self.session():
    # Creates a graph.
    variables.VariableV1(10.0, name="v0")
    # Exports the graph as binary format.
    saver_module.export_meta_graph(filename, as_text=False)
with ops_lib.Graph().as_default(), self.session():
    # Imports the binary format graph.
    saver = saver_module.import_meta_graph(filename)
    self.assertIsNotNone(saver)
    # Exports the graph as text format.
    saver.export_meta_graph(filename, as_text=True)
with ops_lib.Graph().as_default(), self.session():
    # Imports the text format graph.
    saver_module.import_meta_graph(filename)
    # Writes wrong contents to the file.
    graph_io.write_graph(saver.as_saver_def(),
                         os.path.dirname(filename),
                         os.path.basename(filename))
with ops_lib.Graph().as_default(), self.session():
    # Import should fail.
    with self.assertRaisesWithPredicateMatch(IOError,
                                             lambda e: "Cannot parse file"):
        saver_module.import_meta_graph(filename)
    # Deletes the file
    gfile.Remove(filename)
    with self.assertRaisesWithPredicateMatch(IOError,
                                             lambda e: "does not exist"):
        saver_module.import_meta_graph(filename)
