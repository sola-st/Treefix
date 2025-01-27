# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Exits a regular section."""

# Exits are jump nodes, which may be protected.
for exit_ in self.exits[section_id]:
    self.leaves |= self._connect_jump_to_finally_sections(exit_)

del self.exits[section_id]
