# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
source_list = source_utils.list_source_files_against_dump(
    self.dump, node_name_regex_allowlist=r"while/Add.*")

# Assert that the file paths are sorted.
file_paths = [item[0] for item in source_list]
self.assertEqual(sorted(file_paths), file_paths)
self.assertEqual(len(set(file_paths)), len(file_paths))

# Assert that each item of source_list has length 4.
for item in source_list:
    self.assertTrue(isinstance(item, tuple))
    self.assertEqual(6, len(item))

# Due to the node-name filtering the result should only contain 2 nodes
# and 2 tensors. The total number of dumped tensors should be 6:
#   while/Add/y:0          3
#   while/Add:0            3
_, is_tf_py_library, num_nodes, num_tensors, num_dumps, _ = (
    source_list[file_paths.index(self.curr_file_path)])
self.assertFalse(is_tf_py_library)
self.assertEqual(2, num_nodes)
self.assertEqual(2, num_tensors)
self.assertEqual(6, num_dumps)
