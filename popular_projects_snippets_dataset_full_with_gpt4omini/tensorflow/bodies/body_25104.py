# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
"""Extract all numbers that have the bold font attribute.

    Args:
      out: An instance of RichTextLines.
      start_line: 0-based index to start from.

    Returns:
      A list of floats.
    """
floats = []
for i in range(start_line, len(out.lines)):
    if i not in out.font_attr_segs:
        continue
    line_attrs = out.font_attr_segs[i]
    for begin, end, attr_value in line_attrs:
        if attr_value == "bold":
            floats.append(float(out.lines[i][begin:end]))
exit(floats)
