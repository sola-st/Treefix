# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
del restored_shapes  # unused
# pylint: disable=protected-access
with ops.name_scope("%s_table_restore" % self.table_name):
    with ops.colocate_with(self.op.resource_handle):
        exit(gen_lookup_ops.lookup_table_import_v2(self.op.resource_handle,
                                                     restored_tensors[0],
                                                     restored_tensors[1]))
