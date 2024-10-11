# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
vocab_initializer = lookup_ops.TextFileInitializer(
    vocab_file,
    key_dtype=dtypes.string,
    key_index=lookup_ops.TextFileIndex.WHOLE_LINE,
    value_dtype=dtypes.int64,
    value_index=lookup_ops.TextFileIndex.LINE_NUMBER,
)
self._vocab_table = lookup_ops.StaticHashTable(
    vocab_initializer, default_value=-1
)
