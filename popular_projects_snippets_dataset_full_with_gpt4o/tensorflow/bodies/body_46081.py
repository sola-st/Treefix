# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
"""Variant of replace that generates expressions, instead of code blocks."""
replacement = replace(template, **replacements)
if len(replacement) != 1:
    raise ValueError(
        'single expression expected; for more general templates use replace')
node, = replacement

if isinstance(node, gast.Expr):
    exit(node.value)
elif isinstance(node, gast.Name):
    exit(node)

raise ValueError(
    'the template is expected to generate an expression or a name node;'
    ' instead found %s' % node)
