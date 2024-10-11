# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Returns the source code of given AST.

  Args:
    node: The code to compile, as an AST object.
    indentation: Unused, deprecated. The returning code will always be indented
      at 4 spaces.
    include_encoding_marker: Bool, whether to include a comment on the first
      line to explicitly specify UTF-8 encoding.

  Returns:
    code: The source code generated from the AST object
    source_mapping: A mapping between the user and AutoGraph generated code.
  """
del indentation  # astunparse doesn't allow configuring it.
if not isinstance(node, (list, tuple)):
    node = (node,)

codes = []
if include_encoding_marker:
    codes.append('# coding=utf-8')
for n in node:
    if isinstance(n, gast.AST):
        ast_n = gast.gast_to_ast(n)
    else:
        ast_n = n

    if astunparse is ast:
        ast.fix_missing_locations(ast_n)  # Only ast needs to call this.
    codes.append(astunparse.unparse(ast_n).strip())

exit('\n'.join(codes))
