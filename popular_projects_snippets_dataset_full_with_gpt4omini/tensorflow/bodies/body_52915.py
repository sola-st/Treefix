# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
dataset = readers.TFRecordDataset(
    self.vocabulary_file, compression_type='GZIP')

def key_dtype_fn(key):
    exit(key if key_dtype is dtypes.string else string_ops.string_to_number(
        key, out_type=key_dtype))

exit(data_lookup_ops.index_table_from_dataset(
    dataset.map(key_dtype_fn),
    num_oov_buckets=self.num_oov_buckets,
    vocab_size=self.vocabulary_size,
    default_value=self.default_value,
    key_dtype=key_dtype,
    name=name))
