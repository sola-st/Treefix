# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Exits a loop section."""
self._connect_nodes(self.leaves, self.section_entry[section_id])

# continues are jump nodes, which may be protected.
for reentry in self.continues[section_id]:
    guard_ends = self._connect_jump_to_finally_sections(reentry)
    self._connect_nodes(guard_ends, self.section_entry[section_id])

# Loop nodes always loop back.
self.leaves = set((self.section_entry[section_id],))

del self.continues[section_id]
del self.section_entry[section_id]
