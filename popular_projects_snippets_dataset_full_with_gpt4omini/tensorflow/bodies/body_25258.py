# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Add another RichTextLines object to the front.

    Args:
      other: (RichTextLines) The other object to add to the front to this
        object.
    """

other_num_lines = other.num_lines()  # Record original number of lines.

# Merge the lines.
self._lines = other.lines + self._lines

# Merge the font_attr_segs.
new_font_attr_segs = {}
for line_index in self.font_attr_segs:
    new_font_attr_segs[other_num_lines + line_index] = (
        self.font_attr_segs[line_index])
new_font_attr_segs.update(other.font_attr_segs)
self._font_attr_segs = new_font_attr_segs

# Merge the annotations.
new_annotations = {}
for key in self._annotations:
    if isinstance(key, int):
        new_annotations[other_num_lines + key] = (self.annotations[key])
    else:
        new_annotations[key] = other.annotations[key]

new_annotations.update(other.annotations)
self._annotations = new_annotations
