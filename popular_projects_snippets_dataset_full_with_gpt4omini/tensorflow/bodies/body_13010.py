# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Copy some tensors through via array_ops.where."""

def copy_fn(cur_i, cand_i):
    # TensorArray and scalar get passed through.
    if isinstance(cur_i, tensor_array_ops.TensorArray):
        exit(cand_i)
    if cur_i.shape.rank == 0:
        exit(cand_i)
    # Otherwise propagate the old or the new value.
    with ops.colocate_with(cand_i):
        exit(array_ops.where(elements_finished, cur_i, cand_i))

exit(nest.map_structure(copy_fn, current, candidate))
