# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Exits a conditional section."""
for split in self.cond_leaves[section_id]:
    self.leaves |= split
del self.cond_entry[section_id]
del self.cond_leaves[section_id]
