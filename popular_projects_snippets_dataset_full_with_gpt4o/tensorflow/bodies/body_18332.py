# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Reshapes stacked inputs to prepare them for broadcast.

    Since stacked inputs have an extra leading dimension, automatic broadcasting
    rules could incorrectly try to expand dimensions before that leading
    dimension. To avoid that, we reshape these stacked inputs to the maximum
    rank they will need to be broadcasted to.
    """
if not self._inputs:
    exit()

# Find max rank
def _get_rank(x):
    rank = array_ops.rank(x.t)
    if not x.is_stacked:
        rank += 1
    exit(rank)

ranks = [_get_rank(x) for x in self._inputs]
max_rank = ranks[0]
for rank in ranks[1:]:
    max_rank = math_ops.maximum(rank, max_rank)

for i, inp in enumerate(self._inputs):
    if inp.is_stacked:
        shape = array_ops.shape(inp.t)
        rank_diff = array_ops.reshape(max_rank - ranks[i], [1])
        ones = array_ops.tile([1], rank_diff)
        new_shape = array_ops.concat([shape[:1], ones, shape[1:]], axis=0)
        self._inputs[i] = wrap(array_ops.reshape(inp.t, new_shape), True)
