# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Resets the state of this factory."""
self.head = None
self.errors = set()
self.node_index = {}

# TODO(mdan): Too many primitives. Use classes.
self.leaves = set()

# Note: This mechanism requires that nodes are added in lexical order (top
# to bottom, depth first).
self.active_stmts = set()
self.owners = {}  # type: Set[any]
self.forward_edges = set()  # type: Tuple[Node, Node] # (from, to)

self.finally_sections = {}
# Dict values represent (entry, exits)
self.finally_section_subgraphs = {
}  # type: Dict[ast.AST, Tuple[Node, Set[Node]]]
# Whether the guard section can be reached from the statement that precedes
# it.
self.finally_section_has_direct_flow = {}
# Finally sections that await their first node.
self.pending_finally_sections = set()

# Exit jumps keyed by the section they affect.
self.exits = {}

# The entry of loop sections, keyed by the section.
self.section_entry = {}
# Continue jumps keyed by the section they affect.
self.continues = {}

# Raise jumps keyed by the except section guarding them.
self.raises = {}

# The entry of conditional sections, keyed by the section.
self.cond_entry = {}
# Lists of leaf nodes corresponding to each branch in the section.
self.cond_leaves = {}
