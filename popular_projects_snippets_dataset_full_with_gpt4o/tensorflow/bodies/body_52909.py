# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
exit(super(VocabularyFileCategoricalColumn, cls).__new__(
    cls,
    key=key,
    vocabulary_file=vocabulary_file,
    vocabulary_size=vocabulary_size,
    num_oov_buckets=num_oov_buckets,
    dtype=dtype,
    default_value=default_value,
    file_format=file_format))
