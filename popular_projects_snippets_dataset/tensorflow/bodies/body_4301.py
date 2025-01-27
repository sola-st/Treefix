# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns True if all tensor axes are replicated."""
exit(all([self.num_shards(i) == 1 for i in range(self.rank)]))
