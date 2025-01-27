# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
"""Tests whether the CFG contains the specified edges."""
for prev, node_repr, next_ in edges:
    matched = False
    for cfg_node in graph.index.values():
        if repr(cfg_node) == node_repr:
            if (self._as_set(prev) == frozenset(map(repr, cfg_node.prev)) and
                self._as_set(next_) == frozenset(map(repr, cfg_node.next))):
                matched = True
                break
    if not matched:
        self.fail(
            'match failed for node "%s" in graph:\n%s' % (node_repr, graph))
