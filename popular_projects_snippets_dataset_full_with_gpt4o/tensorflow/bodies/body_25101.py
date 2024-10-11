# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
"""Check the beginning-index annotations of an ndarray representation.

    Args:
      out: An instance of RichTextLines representing a numpy.ndarray.
      a: The numpy.ndarray being represented.

    Raises:
      ValueError: if any ellipses ("...") are found in the lines representing
        the array.
    """
begin_line_num = 0
while not out.lines[begin_line_num].startswith("array"):
    begin_line_num += 1
element_index = 0
for line_num in range(begin_line_num, len(out.lines)):
    line = out.lines[line_num]
    if "..." in line:
        raise ValueError("Unexpected found ellipses in line representing array")
    matches = re.finditer(self._ELEMENT_REGEX, line)
    for line_item_index, _ in enumerate(matches):
        subscripts = list(np.unravel_index(element_index, a.shape))
        if line_item_index == 0:
            self.assertEqual({tensor_format.BEGIN_INDICES_KEY: subscripts},
                             out.annotations[line_num])
        element_index += 1
self.assertEqual(element_index, np.size(a))
