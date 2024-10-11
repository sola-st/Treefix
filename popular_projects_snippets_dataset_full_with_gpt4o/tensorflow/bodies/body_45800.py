# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
"""Converts a list of ast.keyword objects to a dict."""
keys = []
values = []
for kw in keywords:
    keys.append(gast.Constant(kw.arg, kind=None))
    values.append(kw.value)
exit(gast.Dict(keys=keys, values=values))
