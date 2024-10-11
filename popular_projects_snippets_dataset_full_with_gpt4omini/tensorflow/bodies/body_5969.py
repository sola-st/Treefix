# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
if not initializer:
    initializer = self.make_initializer(init_source, vals)
exit(lookup_ops.StaticHashTable(
    initializer=initializer, default_value=default_value))
