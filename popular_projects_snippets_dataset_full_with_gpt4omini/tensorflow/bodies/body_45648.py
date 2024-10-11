# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
"""Tests whether the CFG contains the specified statement edges."""
for prev_node_reprs, node_repr, next_node_reprs in edges:
    matched = False
    partial_matches = []
    self.assertSetEqual(
        frozenset(graph.stmt_next.keys()), frozenset(graph.stmt_prev.keys()))
    for stmt_ast_node in graph.stmt_next:
        ast_repr = '%s:%s' % (stmt_ast_node.__class__.__name__,
                              stmt_ast_node.lineno)
        if ast_repr == node_repr:
            actual_next = frozenset(map(repr, graph.stmt_next[stmt_ast_node]))
            actual_prev = frozenset(map(repr, graph.stmt_prev[stmt_ast_node]))
            partial_matches.append((actual_prev, node_repr, actual_next))
            if (self._as_set(prev_node_reprs) == actual_prev and
                self._as_set(next_node_reprs) == actual_next):
                matched = True
                break
    if not matched:
        self.fail('edges mismatch for %s: %s' % (node_repr, partial_matches))
