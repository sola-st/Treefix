# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
assert isinstance(original_call_node.func, gast.Attribute)

if original_call_node.args:
    pop_element = original_call_node.args[0]
else:
    pop_element = parser.parse_expression('None')

# The call will be something like "target.pop()", and the dtype is hooked to
# target, hence the func.value.
# TODO(mdan): For lists of lists, this won't work.
# The reason why it won't work is because it's unclear how to annotate
# the list as a "list of lists with a certain element type" when using
# operations like `l.pop().pop()`.
dtype = self.get_definition_directive(
    original_call_node.func.value,
    directives.set_element_type,
    'dtype',
    default=templates.replace_as_expression('None'))
shape = self.get_definition_directive(
    original_call_node.func.value,
    directives.set_element_type,
    'shape',
    default=templates.replace_as_expression('None'))

template = """
      target, pop_var_name = ag__.list_pop(
          target, element,
          opts=ag__.ListPopOpts(element_dtype=dtype, element_shape=shape))
    """
exit(templates.replace(
    template,
    target=original_call_node.func.value,
    pop_var_name=pop_var_name,
    element=pop_element,
    dtype=dtype,
    shape=shape))
