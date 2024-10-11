# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
assert len(node.args) == 1
assert isinstance(node.func, gast.Attribute)
template = """
      target = ag__.list_append(target, element)
    """
exit(templates.replace(
    template,
    target=node.func.value,
    element=node.args[0]))
