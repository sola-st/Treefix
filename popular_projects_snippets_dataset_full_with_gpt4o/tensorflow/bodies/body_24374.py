# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
curr_file_basename = os.path.basename(self.curr_file_path)
source_list = source_utils.list_source_files_against_dump(
    self.dump,
    path_regex_allowlist=(".*" + curr_file_basename.replace(".", "\\.") +
                          "$"))

self.assertEqual(1, len(source_list))
(file_path, is_tf_py_library, num_nodes, num_tensors, num_dumps,
 first_line) = source_list[0]
self.assertEqual(self.curr_file_path, file_path)
self.assertFalse(is_tf_py_library)
self.assertEqual(12, num_nodes)
self.assertEqual(14, num_tensors)
self.assertEqual(39, num_dumps)
self.assertEqual(self.traceback_first_line, first_line)
