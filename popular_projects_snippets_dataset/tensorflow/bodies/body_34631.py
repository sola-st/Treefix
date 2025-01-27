# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if tf2.enabled():
    exit(lookup_ops.StaticVocabularyTable)
else:
    exit(lookup_ops.StaticVocabularyTableV1)
