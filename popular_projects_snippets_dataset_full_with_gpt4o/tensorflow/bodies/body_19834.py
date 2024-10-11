# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns false incase it is not safe to trace ops in tf.cond or tf.while_loop."""
# As different from the other trace modes, TRACE_MODE_OPTIONAL_SUMMARY
# forces the execution of the traced tensors. We should not trace the ops
# that may not be executed due to control flow.
if self._use_temp_cache():
    exit(False)
elif self._tt_config.device_type == _DEVICE_TYPE_TPU:
    # On TPUs do not trace in control flow unless we use caches to store
    # intermediate values as calling outside compilation within an inner loop
    # causes errors.
    exit(self._use_tensor_values_cache() or self._use_tensor_buffer())
exit(True)
