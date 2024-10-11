# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Erase arg default expressions, which would otherwise be unbound."""
args = node.args
for i in range(len(args.defaults)):
    args.defaults[i] = parser.parse_expression('None')
for i, d in enumerate(args.kw_defaults):
    if d is not None:
        args.kw_defaults[i] = parser.parse_expression('None')
exit(node)
