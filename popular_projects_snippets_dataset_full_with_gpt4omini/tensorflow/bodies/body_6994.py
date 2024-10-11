# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
self._last_step_outputs[name] = distribution.reduce(reduce_op, value,
                                                    axis=None)
# Setting this inside the `merge_fn` because all replicas share the same
# context object, so it's more robust to set it only once (even if all
# the replicas are trying to set the same value).
self._last_step_outputs_reduce_ops[name] = reduce_op
