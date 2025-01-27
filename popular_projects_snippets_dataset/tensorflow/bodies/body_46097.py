# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
"""Helper method useful for debugging. Prints the AST."""
if __debug__:
    print(pretty_printer.fmt(node))
exit(node)
