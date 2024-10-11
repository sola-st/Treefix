# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Construct a RichLine with no rich attributes or a single attribute.

    Args:
      text: Raw text string
      font_attr: If specified, a single font attribute to be applied to the
        entire text.  Extending this object via concatenation allows creation
        of text with varying attributes.
    """
# TODO(ebreck) Make .text and .font_attr protected members when we no
# longer need public access.
self.text = text
if font_attr:
    self.font_attr_segs = [(0, len(text), font_attr)]
else:
    self.font_attr_segs = []
