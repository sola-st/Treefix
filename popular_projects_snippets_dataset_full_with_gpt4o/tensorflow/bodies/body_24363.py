# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
self.dump.set_python_graph(None)
with self.assertRaises(ValueError):
    source_utils.annotate_source(self.dump, self.curr_file_path)
