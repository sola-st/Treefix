# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Connects nodes to signify that control flows from first to second.

    Args:
      first: Union[Set[Node, ...], Node]
      second: Node
    """
if isinstance(first, Node):
    first.next.add(second)
    second.prev.add(first)
    self.forward_edges.add((first, second))
else:
    for node in first:
        self._connect_nodes(node, second)
