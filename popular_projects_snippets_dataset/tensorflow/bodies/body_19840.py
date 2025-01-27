# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Creates a temporary cache with the given dimensions.

    Fills the self._temp_cache_var with num_traced_tensors tf.constant() ops
    that have shape of [num_signatures].
    Args:
      num_traced_tensors: Int, denoting total number of traced tensors.
      num_signatures: Int, denoting the number of statistics collected per
        tensors.
      graph: TensorFlow graph.
    """
init_value = constant_op.constant(_COMPACT_TRACE_ENTRY_INIT_VALUE,
                                  dtype=dtypes.float32,
                                  shape=[num_signatures])
self._temp_cache_var[graph] = [
    init_value for _ in range(num_traced_tensors)]
