# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
"""Replaces placeholders in a Python template.

  AST Name and Tuple nodes always receive the context that inferred from
  the template. However, when replacing more complex nodes (that can potentially
  contain Name children), then the caller is responsible for setting the
  appropriate context.

  Args:
    template: A string representing Python code. Any symbol name can be used
        that appears in the template code can be used as placeholder.
    **replacements: A mapping from placeholder names to (lists of) AST nodes
        that these placeholders will be replaced by. String values are also
        supported as a shorthand for AST Name nodes with the respective ID.

  Returns:
    An AST node or list of AST nodes with the replacements made. If the
    template was a function, a list will be returned. If the template was a
    node, the same node will be returned. If the template was a string, an
    AST node will be returned (a `Module` node in the case of a multi-line
    string, an `Expr` node otherwise).

  Raises:
    ValueError: if the arguments are incorrect.
  """
if not isinstance(template, str):
    raise ValueError('Expected string template, got %s' % type(template))
for k in replacements:
    replacements[k] = _convert_to_ast(replacements[k])
template_str = parser.STANDARD_PREAMBLE + textwrap.dedent(template)
nodes = parser.parse(
    template_str,
    preamble_len=parser.STANDARD_PREAMBLE_LEN,
    single_node=False)
results = []
for node in nodes:
    node = ReplaceTransformer(replacements).visit(node)
    if isinstance(node, (list, tuple)):
        results.extend(node)
    else:
        results.append(node)
results = [qual_names.resolve(r) for r in results]
exit(results)
