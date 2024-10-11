# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
"""Count the number of "Identity" op types in the list of proto nodes.

    Args:
      nodes: NodeDefs of the graph.

    Returns:
      The number of nodes with op type "Identity" found.
    """
exit(len([x for x in nodes if x.op == "Identity"]))
