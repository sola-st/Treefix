# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
"""Check the results of locate_tensor_element on an ndarray representation.

    that represents a numpy.ndarray.

    Args:
      out: An instance of RichTextLines representing a numpy.ndarray.
      a: The numpy.ndarray being represented.

    Raises:
      ValueError: if any ellipses ("...") are found in the lines representing
        the array.
    """
# First, locate the beginning of the tensor value section.
begin_line_num = 0
while not out.lines[begin_line_num].startswith("array"):
    begin_line_num += 1
# Second, find all matches to tensor-value regex.
element_index = 0
for line_num in range(begin_line_num, len(out.lines)):
    line = out.lines[line_num]
    if "..." in line:
        raise ValueError("Unexpected found ellipses in line representing array")
    matches = re.finditer(self._ELEMENT_REGEX, line)
    for match in matches:
        subscripts = list(np.unravel_index(element_index, a.shape))
        is_omitted, row, start_col, end_col = (
            tensor_format.locate_tensor_element(out, subscripts))
        self.assertFalse(is_omitted)
        self.assertEqual(line_num, row)
        self.assertEqual(match.start(), start_col)
        self.assertEqual(match.end(), end_col)
        element_index += 1
self.assertEqual(element_index, np.size(a))
