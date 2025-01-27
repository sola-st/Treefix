# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Mapping from offset to index in global tensor."""
index = 0
for i, o in enumerate(offset_tuple):
    m = 1
    for x in range(i + 1, self.rank):
        m = m * self.num_shards(x)
    index = index + m * o
exit(index)
