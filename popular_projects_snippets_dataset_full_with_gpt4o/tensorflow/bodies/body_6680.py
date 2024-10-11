# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
"""Returns whether each of the underlying variables is replicated or sharded to logical cores.

    If True, the handles of the underlying variables are not available outside a
    TPU context.
    """
exit(isinstance(self._primary,
                  tpu_replicated_variable.TPUReplicatedVariable))
