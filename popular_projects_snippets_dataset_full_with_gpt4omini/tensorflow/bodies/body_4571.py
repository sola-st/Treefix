# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/simple_hash_table/simple_hash_table.py
"""Implements checkpointing protocols for `Trackable`."""
tensors = self.export()
exit({"table-keys": tensors[0], "table-values": tensors[1]})
