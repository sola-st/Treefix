# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
timestamp_col_width, dump_size_col_width, op_type_col_width = (
    self._analyzer._measure_tensor_list_column_widths([]))
self.assertEqual(len("t (ms)") + 1, timestamp_col_width)
self.assertEqual(len("Size (B)") + 1, dump_size_col_width)
self.assertEqual(len("Op type") + 1, op_type_col_width)
