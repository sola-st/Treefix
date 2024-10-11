# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = (np.arange(11 * 11 * 11) + 1000).reshape([11, 11, 11]).astype(np.int32)

out = tensor_format.format_tensor(
    a, "a", False, np_printoptions={"threshold": 100,
                                    "edgeitems": 2})

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
self.assertEqual(repr(a).split("\n"), out.lines[2:])

actual_row_0_0_0, actual_col_0_0_0 = self._findFirst(out.lines, "1000")
actual_row_0_0_10, _ = self._findFirst(out.lines, "1010")
actual_row_10_10_10, _ = self._findFirst(out.lines, "2330")

(are_omitted, rows, start_cols,
 end_cols) = tensor_format.locate_tensor_element(out, [[0, 0, 0]])
self.assertEqual([False], are_omitted)
self.assertEqual([actual_row_0_0_0], rows)
self.assertEqual([actual_col_0_0_0], start_cols)
self.assertEqual([actual_col_0_0_0 + 4], end_cols)

(are_omitted, rows, start_cols,
 end_cols) = tensor_format.locate_tensor_element(out,
                                                 [[0, 0, 0], [0, 0, 10]])
self.assertEqual([False, False], are_omitted)
self.assertEqual([actual_row_0_0_0, actual_row_0_0_10], rows)
self.assertEqual([actual_col_0_0_0, None], start_cols)
self.assertEqual([actual_col_0_0_0 + 4, None], end_cols)

(are_omitted, rows, start_cols,
 end_cols) = tensor_format.locate_tensor_element(out,
                                                 [[0, 0, 0], [0, 2, 0]])
self.assertEqual([False, True], are_omitted)
self.assertEqual([2, 4], rows)
self.assertEqual(2, len(start_cols))
self.assertEqual(2, len(end_cols))

(are_omitted, rows, start_cols,
 end_cols) = tensor_format.locate_tensor_element(out,
                                                 [[0, 0, 0], [10, 10, 10]])
self.assertEqual([False, False], are_omitted)
self.assertEqual([actual_row_0_0_0, actual_row_10_10_10], rows)
self.assertEqual([actual_col_0_0_0, None], start_cols)
self.assertEqual([actual_col_0_0_0 + 4, None], end_cols)
