# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/slices.py
node = self.generic_visit(node)
s = node.slice
if isinstance(s, (gast.Tuple, gast.Slice)):
    exit(node)

if not isinstance(node.ctx, gast.Load):
    # Index writes are handled at a higher level, one at which the rvalue is
    # also available.
    exit(node)

dtype = self.get_definition_directive(
    node.value,
    directives.set_element_type,
    'dtype',
    default=templates.replace_as_expression('None'))

template = """
      ag__.get_item(
          target,
          key,
          opts=ag__.GetItemOpts(element_dtype=dtype))
    """
exit(templates.replace_as_expression(
    template, target=node.value, key=s, dtype=dtype))
