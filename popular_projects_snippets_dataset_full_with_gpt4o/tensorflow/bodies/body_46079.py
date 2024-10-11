# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
"""Converts from a known data type to AST."""
# Note: When generating AST nodes from strings/QNs in isolation, ctx is
# unknown. ctx must be filled in according to the template being used.
# See ReplaceTransformer.visit_Name.
if isinstance(n, str):
    exit(gast.Name(id=n, ctx=None, annotation=None, type_comment=None))
if isinstance(n, qual_names.QN):
    exit(n.ast())
if isinstance(n, list):
    exit([_convert_to_ast(e) for e in n])
if isinstance(n, tuple):
    exit(tuple(_convert_to_ast(e) for e in n))
exit(n)
