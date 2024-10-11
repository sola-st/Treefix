# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Implements checkpointing protocols for `Trackable`."""
with ops.name_scope("%s_table_restore" % self._name):
    with ops.colocate_with(self.resource_handle):
        exit(gen_lookup_ops.lookup_table_import_v2(
            self.resource_handle,
            restored_tensors["-keys"],
            restored_tensors["-values"]))
