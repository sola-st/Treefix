# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Begins a new branch in a cond section."""
assert section_id in self.cond_leaves

if section_id in self.cond_entry:
    # Subsequent splits move back to the split point, and memorize the
    # current leaves.
    self.cond_leaves[section_id].append(self.leaves)
    self.leaves = self.cond_entry[section_id]
else:
    # If this is the first time we split a section, just remember the split
    # point.
    self.cond_entry[section_id] = self.leaves
