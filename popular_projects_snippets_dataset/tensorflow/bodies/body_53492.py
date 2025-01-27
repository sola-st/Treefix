# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Check if the graph is finalized.

    Raises:
      RuntimeError: If the graph finalized.
    """
if self._finalized:
    raise RuntimeError("Graph is finalized and cannot be modified.")
