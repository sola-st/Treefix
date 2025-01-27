# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
test_dir = _TestDir("scoped_with_queue")
orig_meta_graph = self._testScopedExportWithQueue(test_dir,
                                                  "exported_queue1.pbtxt")
new_meta_graph = self._testScopedImportWithQueue(
    test_dir, "exported_queue1.pbtxt", "exported_new_queue1.pbtxt")
test_util.assert_meta_graph_protos_equal(self, orig_meta_graph,
                                         new_meta_graph)
