# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
assert len(node.args) == 1
dtype = self.get_definition_directive(
    node.args[0],
    directives.set_element_type,
    'dtype',
    default=templates.replace_as_expression('None'))
template = """
      ag__.list_stack(
          target,
          opts=ag__.ListStackOpts(
              element_dtype=dtype,
              original_call=orig_call))
    """
exit(templates.replace_as_expression(
    template,
    dtype=dtype,
    target=node.args[0],
    orig_call=node.func))
