# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
if tf2.enabled():
    exit(core_lookup_ops.StaticHashTable)
else:
    exit(core_lookup_ops.StaticHashTableV1)
