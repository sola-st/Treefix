# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Performs an actual transformation of a function's AST.

    Subclasses must implement this method, and do not usually call it.

    Args:
      node: One or more ast.AST nodes representing the AST to be transformed.
      ctx: transformer.Context.
    """
raise NotImplementedError('subclasses must override this')
