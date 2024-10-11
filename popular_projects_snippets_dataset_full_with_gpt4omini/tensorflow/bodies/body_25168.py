# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
dump = self._debug_dump.dumped_tensor_data[0]
self.assertLess(dump.dump_size_bytes, 1000)
self.assertEqual(
    "VariableV2", self._debug_dump.node_op_type(dump.node_name))
_, dump_size_col_width, op_type_col_width = (
    self._analyzer._measure_tensor_list_column_widths([dump]))
# The length of str(dump.dump_size_bytes) is less than the length of
# "Size (B)" (8). So the column width should be determined by the length of
# "Size (B)".
self.assertEqual(len("Size (B)") + 1, dump_size_col_width)
# The length of "VariableV2" is greater than the length of "Op type". So the
# column should be determined by the length of "VariableV2".
self.assertEqual(len("VariableV2") + 1, op_type_col_width)
