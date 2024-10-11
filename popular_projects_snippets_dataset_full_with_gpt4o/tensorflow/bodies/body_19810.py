# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns true if the intermediate values should be stacked instead of being stored in a tf.Variable.

    Returns:
      A boolean, denoting whether to use a temporary cache or not.
    """
# If full tensors need to be stored tf.variables, then do not use temp
# variables to store them.
if self._use_tensor_buffer():
    exit(False)
if self._use_tensor_values_cache():
    exit(self._parameters.use_temp_cache_var)
else:
    # Temporary caches only replaces tf.Variables caches. If no cache is used
    # return False.
    exit(False)
