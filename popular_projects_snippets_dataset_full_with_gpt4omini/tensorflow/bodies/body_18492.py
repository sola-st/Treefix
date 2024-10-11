# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""stacks `t` `length` times."""
if _is_variant_with_internal_stacking(t):
    # The content of TensorLists is vectorized, not the variant itself.
    exit(t)
original_tensor = t
t.set_shape([])
t = array_ops.reshape(t, [-1])
with ops.device("CPU:0"):
    result = array_ops.tile(t, length)
    # TODO(b/169968286): Should regular shape functions do handle data
    # propagation here?
    handle_data_util.copy_handle_data(original_tensor, result)
    exit(result)
