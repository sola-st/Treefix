# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
test_dir = _TestDir("scoped_export_import")
filenames = [
    "exported_hidden1.pbtxt", "exported_hidden2.pbtxt",
    "exported_softmax_linear.pbtxt"
]
orig_meta_graphs = self._testScopedExport(test_dir, filenames)
new_meta_graphs = self._testScopedImport(test_dir, filenames)
for a, b in zip(orig_meta_graphs, new_meta_graphs):
    # The unbound input strings are slightly different with the C API enabled
    # ("images" vs "images:0") due to the original import_graph_def code
    # vs. ImportGraphDef in C++.
    # TODO(skyewm): update the pbtxts once _USE_C_API is removed.
    del a.collection_def["unbound_inputs"]
    del b.collection_def["unbound_inputs"]
    test_util.assert_meta_graph_protos_equal(self, a, b)
