# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/slices.py
if not isinstance(target, gast.Subscript):
    exit(None)
s = target.slice
if isinstance(s, (gast.Tuple, gast.Slice)):
    exit(None)

template = """
      target = ag__.set_item(target, key, item)
    """
exit(templates.replace(
    template, target=target.value, key=target.slice, item=value))
