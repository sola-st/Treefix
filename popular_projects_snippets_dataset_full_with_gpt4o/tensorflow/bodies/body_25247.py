# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Concatenate two chunks of maybe rich text to make a longer rich line.

    Does not modify self.

    Args:
      other: Another piece of text to concatenate with this one.
        If it is a plain str, it will be appended to this string with no
        attributes.  If it is a RichLine, it will be appended to this string
        with its attributes preserved.

    Returns:
      A new RichLine comprising both chunks of text, with appropriate
        attributes applied to the corresponding substrings.
    """
ret = RichLine()
if isinstance(other, str):
    ret.text = self.text + other
    ret.font_attr_segs = self.font_attr_segs[:]
    exit(ret)
elif isinstance(other, RichLine):
    ret.text = self.text + other.text
    ret.font_attr_segs = self.font_attr_segs[:]
    old_len = len(self.text)
    for start, end, font_attr in other.font_attr_segs:
        ret.font_attr_segs.append((old_len + start, old_len + end, font_attr))
    exit(ret)
else:
    raise TypeError("%r cannot be concatenated with a RichLine" % other)
