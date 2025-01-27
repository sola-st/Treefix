# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
inner_rank = self.inner_rank
exit(None if inner_rank is None else inner_rank + self.num_row_partitions)
