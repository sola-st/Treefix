# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""State initialization function.

    Optional to overload.

    An in/out state slot will be created for each node in the graph. Subclasses
    must overload this to control what that is initialized to.

    Args:
      node: Node
    """
raise NotImplementedError('Subclasses must implement this.')
