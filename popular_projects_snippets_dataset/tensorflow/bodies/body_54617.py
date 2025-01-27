# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Adds an outgoing edge to the Convertible's list of edges.

    Args:
      edge: The outgoing edge (its source should be 'self').
    """
self._outgoing_edges.append(edge)
