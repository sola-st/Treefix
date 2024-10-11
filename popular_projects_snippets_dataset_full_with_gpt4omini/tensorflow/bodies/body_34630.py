# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if tf2.enabled():
    exit(lookup_ops.StaticHashTable)
else:
    exit(lookup_ops.StaticHashTableV1)
