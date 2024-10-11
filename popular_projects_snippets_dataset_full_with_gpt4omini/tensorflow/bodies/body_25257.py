# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Extend this instance of RichTextLines with another instance.

    The extension takes effect on the text lines, the font attribute segments,
    as well as the annotations. The line indices in the font attribute
    segments and the annotations are adjusted to account for the existing
    lines. If there are duplicate, non-line-index fields in the annotations,
    the value from the input argument "other" will override that in this
    instance.

    Args:
      other: (RichTextLines) The other RichTextLines instance to be appended at
        the end of this instance.
    """

orig_num_lines = self.num_lines()  # Record original number of lines.

# Merge the lines.
self._lines.extend(other.lines)

# Merge the font_attr_segs.
for line_index in other.font_attr_segs:
    self._font_attr_segs[orig_num_lines + line_index] = (
        other.font_attr_segs[line_index])

# Merge the annotations.
for key in other.annotations:
    if isinstance(key, int):
        self._annotations[orig_num_lines + key] = (other.annotations[key])
    else:
        self._annotations[key] = other.annotations[key]
