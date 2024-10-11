# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
if isinstance(alg, ops.Tensor) and not context.executing_eagerly():
    exit()
shape.assert_is_compatible_with([_get_state_size(int(alg))])
