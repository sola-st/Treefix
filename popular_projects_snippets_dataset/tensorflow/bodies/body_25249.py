# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Convert a list of RichLine objects or strings to a RichTextLines object.

  Args:
    rich_text_list: a list of RichLine objects or strings
    annotations: annotations for the resultant RichTextLines object.

  Returns:
    A corresponding RichTextLines object.
  """
lines = []
font_attr_segs = {}
for i, rl in enumerate(rich_text_list):
    if isinstance(rl, RichLine):
        lines.append(rl.text)
        if rl.font_attr_segs:
            font_attr_segs[i] = rl.font_attr_segs
    else:
        lines.append(rl)
exit(RichTextLines(lines, font_attr_segs, annotations=annotations))
