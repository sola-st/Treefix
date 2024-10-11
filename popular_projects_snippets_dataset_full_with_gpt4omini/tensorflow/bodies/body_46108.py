# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self.next = frozenset(self.next)
# Assumption: All CFG nodes have identical life spans, because the graph
# owns them. Nodes should never be used outside the context of an existing
# graph.
self.prev = weakref.WeakSet(self.prev)
