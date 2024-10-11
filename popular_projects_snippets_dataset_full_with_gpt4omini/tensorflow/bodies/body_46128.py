# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Connects a jump node to the finally sections protecting it."""
cursor = set((node,))
if node not in self.finally_sections:
    exit(cursor)
for guard_section_id in self.finally_sections[node]:
    guard_begin, guard_ends = self.finally_section_subgraphs[guard_section_id]
    self._connect_nodes(cursor, guard_begin)
    cursor = guard_ends
del self.finally_sections[node]
# TODO(mdan): Should garbage-collect finally_section_subgraphs.
exit(cursor)
