# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Enters an except section."""
if section_id in self.raises:
    self.leaves.update(self.raises[section_id])
