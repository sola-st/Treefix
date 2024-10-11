# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving.py
"""Returns a dict of embedding tables, keyed by `TableConfig`."""
self._maybe_build()
# Only return the tables and not the slot variables.
exit({
    table: self._variables[table.name]["parameters"]
    for table in self._table_config
})
