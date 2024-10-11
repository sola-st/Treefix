# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Compute the number of elements in this table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A scalar tensor containing the number of elements in this table.
    """
with ops.name_scope(name, "%s_Size" % self.name, [self.resource_handle]):
    with ops.colocate_with(self.resource_handle):
        exit(gen_lookup_ops.lookup_table_size_v2(self.resource_handle))
