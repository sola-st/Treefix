# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
"""Ties together all keyword and **kwarg arguments in a single dict."""
if node.keywords:
    exit(gast.Call(
        gast.Name(
            'dict', ctx=gast.Load(), annotation=None, type_comment=None),
        args=(),
        keywords=node.keywords))
else:
    exit(parser.parse_expression('None'))
