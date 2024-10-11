# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
source_list = source_utils.list_source_files_against_dump(self.dump)

# Assert that the file paths are sorted and unique.
file_paths = [item[0] for item in source_list]
self.assertEqual(sorted(file_paths), file_paths)
self.assertEqual(len(set(file_paths)), len(file_paths))

# Assert that each item of source_list has length 6.
for item in source_list:
    self.assertTrue(isinstance(item, tuple))
    self.assertEqual(6, len(item))

# The while loop body should have executed 3 times. The following table
# lists the tensors and how many times each of them is dumped.
#   Tensor name            # of times dumped:
#   i:0                    1
#   while/Enter:0          1
#   while/Merge:0          4
#   while/Merge:1          4
#   while/Less/y:0         4
#   while/Less:0           4
#   while/LoopCond:0       4
#   while/Switch:0         1
#   while/Switch:1         3
#   while/Identity:0       3
#   while/Add/y:0          3
#   while/Add:0            3
#   while/NextIteration:0  3
#   while/Exit:0           1
# ----------------------------
#   (Total)                39
#
# The total number of nodes is 12.
# The total number of tensors is 14 (2 of the nodes have 2 outputs:
#   while/Merge, while/Switch).

_, is_tf_py_library, num_nodes, num_tensors, num_dumps, first_line = (
    source_list[file_paths.index(self.curr_file_path)])
self.assertFalse(is_tf_py_library)
self.assertEqual(12, num_nodes)
self.assertEqual(14, num_tensors)
self.assertEqual(39, num_dumps)
self.assertEqual(self.traceback_first_line, first_line)
