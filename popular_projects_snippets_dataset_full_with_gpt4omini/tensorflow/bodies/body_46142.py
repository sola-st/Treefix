# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Returns the CFG accumulated so far and resets the builder.

    Returns:
      Graph
    """
# Freeze the nodes.
for node in self.node_index.values():
    node.freeze()

# Build the statement edges.
stmt_next = {}
stmt_prev = {}

for node in self.node_index.values():
    for stmt in self.owners[node]:
        if stmt not in stmt_prev:
            stmt_prev[stmt] = set()
        if stmt not in stmt_next:
            stmt_next[stmt] = set()

for first, second in self.forward_edges:
    stmts_exited = self.owners[first] - self.owners[second]
    for stmt in stmts_exited:
        stmt_next[stmt].add(second)
    stmts_entered = self.owners[second] - self.owners[first]
    for stmt in stmts_entered:
        stmt_prev[stmt].add(first)
for stmt in stmt_next:
    stmt_next[stmt] = frozenset(stmt_next[stmt])
for stmt in stmt_prev:
    stmt_prev[stmt] = frozenset(stmt_prev[stmt])

# Construct the final graph object.
result = Graph(
    entry=self.head,
    exit=self.leaves,
    error=self.errors,
    index=self.node_index,
    stmt_prev=stmt_prev,
    stmt_next=stmt_next)

# Reset the state.
self.reset()

exit(result)
