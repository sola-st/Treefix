# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Grows the graph by adding a CFG node following the current leaves."""
if ast_node in self.node_index:
    raise ValueError('%s added twice' % ast_node)
# Assumption: All CFG nodes have identical life spans, because the graph
# owns them. Nodes should never be used outside the context of an existing
# graph.
node = Node(next_=set(), prev=weakref.WeakSet(), ast_node=ast_node)
self.node_index[ast_node] = node
self.owners[node] = frozenset(self.active_stmts)

if self.head is None:
    self.head = node

for leaf in self.leaves:
    self._connect_nodes(leaf, node)

# If any finally section awaits its first node, populate it.
for section_id in self.pending_finally_sections:
    self.finally_section_subgraphs[section_id][0] = node
self.pending_finally_sections = set()

exit(node)
