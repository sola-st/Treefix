# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
"""Helper method useful for debugging. Prints the AST as code."""
if __debug__:
    print(parser.unparse(node))
exit(node)
