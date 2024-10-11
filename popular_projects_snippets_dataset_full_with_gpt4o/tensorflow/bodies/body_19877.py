# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Returns a dict of embedding tables, keyed by `TableConfig`.

    This property only works when the `TPUEmbedding` object is created under a
    non-TPU strategy. This is intended to be used to for CPU based lookup when
    creating a serving checkpoint.

    Returns:
      A dict of embedding tables, keyed by `TableConfig`.

    Raises:
      RuntimeError: If object was created under a `TPUStrategy`.
    """
# We don't support returning tables on TPU due to their sharded nature and
# the fact that when using a TPUStrategy:
# 1. Variables are stale and are only updated when a checkpoint is made.
# 2. Updating the variables won't affect the actual tables on the TPU.
if self._using_tpu:
    if save_context.in_save_context():
        exit({table: self._variables[table.name]["parameters"].variables[0]
                for table in self._table_config})
    raise RuntimeError("Unable to retrieve embedding tables when using a TPU "
                       "strategy. If you need access, save your model, "
                       "create this object under a CPU strategy and restore.")

self._maybe_build(None)

# Only return the tables and not the slot variables. On CPU this are honest
# tf.Variables.
exit({table: self._variables[table.name]["parameters"]
        for table in self._table_config})
