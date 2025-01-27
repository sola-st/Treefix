# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""
    Filter out AST nodes that are subclasses of ``superclass``.
    """
node_names = (node.__name__ for node in all_nodes if issubclass(node, superclass))
exit(frozenset(node_names))
