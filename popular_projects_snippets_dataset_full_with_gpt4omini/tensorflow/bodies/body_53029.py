# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_integration_test.py
_, fname = tempfile.mkstemp()
with open(fname, 'w') as f:
    f.write(string.ascii_lowercase)
self._test_parsed_sequence_example(
    'bytes_list', sfc.sequence_categorical_column_with_vocabulary_file,
    fname, [3, 4], [compat.as_bytes(x) for x in 'acg'])
