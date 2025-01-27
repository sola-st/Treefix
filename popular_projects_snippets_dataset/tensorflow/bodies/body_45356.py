# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/list_comprehensions.py
if not isinstance(node.value, gast.ListComp):
    exit(self.generic_visit(node))
if len(node.targets) > 1:
    raise NotImplementedError('multiple assignments')

target, = node.targets
list_comp_node = node.value

template = """
      target = []
    """
initialization = templates.replace(template, target=target)

template = """
      target.append(elt)
    """
body = templates.replace(template, target=target, elt=list_comp_node.elt)

for gen in reversed(list_comp_node.generators):
    for gen_if in reversed(gen.ifs):
        template = """
          if test:
            body
        """
        body = templates.replace(template, test=gen_if, body=body)
    template = """
        for target in iter_:
          body
      """
    body = templates.replace(
        template, iter_=gen.iter, target=gen.target, body=body)

exit(initialization + body)
