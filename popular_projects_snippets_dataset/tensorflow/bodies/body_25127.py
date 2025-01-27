# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = (np.arange(11 * 11 * 11) + 1000).reshape([11, 11, 11]).astype(np.int32)

out = tensor_format.format_tensor(
    a, "a", False, np_printoptions={"threshold": 100, "edgeitems": 2})

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])

actual_row_0_0_0, actual_col_0_0_0 = self._findFirst(out.lines, "1000")
is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [0, 0, 0])
self.assertFalse(is_omitted)
self.assertEqual(actual_row_0_0_0, row)
self.assertEqual(actual_col_0_0_0, start_col)
self.assertEqual(actual_col_0_0_0 + 4, end_col)

actual_row_0_0_10, _ = self._findFirst(out.lines, "1010")
is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [0, 0, 10])
self.assertFalse(is_omitted)
self.assertEqual(actual_row_0_0_10, row)
self.assertIsNone(start_col)  # Passes ellipsis.
self.assertIsNone(end_col)

actual_row_0_1_0, actual_col_0_1_0 = self._findFirst(out.lines, "1011")
is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [0, 1, 0])
self.assertFalse(is_omitted)
self.assertEqual(actual_row_0_1_0, row)
self.assertEqual(actual_col_0_1_0, start_col)
self.assertEqual(actual_col_0_1_0 + 4, end_col)

is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [0, 2, 0])
self.assertTrue(is_omitted)  # In omitted line.
self.assertIsNone(start_col)
self.assertIsNone(end_col)

is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [0, 2, 10])
self.assertTrue(is_omitted)  # In omitted line.
self.assertIsNone(start_col)
self.assertIsNone(end_col)

is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [0, 8, 10])
self.assertTrue(is_omitted)  # In omitted line.
self.assertIsNone(start_col)
self.assertIsNone(end_col)

actual_row_0_10_1, actual_col_0_10_1 = self._findFirst(out.lines, "1111")
is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [0, 10, 1])
self.assertFalse(is_omitted)
self.assertEqual(actual_row_0_10_1, row)
self.assertEqual(actual_col_0_10_1, start_col)
self.assertEqual(actual_col_0_10_1 + 4, end_col)

is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [5, 1, 1])
self.assertTrue(is_omitted)  # In omitted line.
self.assertIsNone(start_col)
self.assertIsNone(end_col)

actual_row_10_10_10, _ = self._findFirst(out.lines, "2330")
is_omitted, row, start_col, end_col = tensor_format.locate_tensor_element(
    out, [10, 10, 10])
self.assertFalse(is_omitted)
self.assertEqual(actual_row_10_10_10, row)
self.assertIsNone(start_col)  # Past ellipsis.
self.assertIsNone(end_col)

with self.assertRaisesRegex(ValueError, "Indices exceed tensor dimensions"):
    tensor_format.locate_tensor_element(out, [11, 5, 5])

with self.assertRaisesRegex(ValueError, "Indices contain negative"):
    tensor_format.locate_tensor_element(out, [-1, 5, 5])

with self.assertRaisesRegex(ValueError, "Dimensions mismatch"):
    tensor_format.locate_tensor_element(out, [5, 5])
