# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Slice a RichTextLines object.

    The object itself is not changed. A sliced instance is returned.

    Args:
      begin: (int) Beginning line index (inclusive). Must be >= 0.
      end: (int) Ending line index (exclusive). Must be >= 0.

    Returns:
      (RichTextLines) Sliced output instance of RichTextLines.

    Raises:
      ValueError: If begin or end is negative.
    """

if begin < 0 or end < 0:
    raise ValueError("Encountered negative index.")

# Copy lines.
lines = self.lines[begin:end]

# Slice font attribute segments.
font_attr_segs = {}
for key in self.font_attr_segs:
    if key >= begin and key < end:
        font_attr_segs[key - begin] = self.font_attr_segs[key]

    # Slice annotations.
annotations = {}
for key in self.annotations:
    if not isinstance(key, int):
        # Annotations can contain keys that are not line numbers.
        annotations[key] = self.annotations[key]
    elif key >= begin and key < end:
        annotations[key - begin] = self.annotations[key]

exit(RichTextLines(
    lines, font_attr_segs=font_attr_segs, annotations=annotations))
