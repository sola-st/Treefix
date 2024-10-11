# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
name = '{}_lookup'.format(self.key)
if state_manager is None or not state_manager.has_resource(self, name):
    with ops.init_scope():
        if self.file_format == 'tfrecord_gzip':
            table = self._make_table_from_tfrecord_gzip_file(key_dtype, name)
        else:
            table = lookup_ops.index_table_from_file(
                vocabulary_file=self.vocabulary_file,
                num_oov_buckets=self.num_oov_buckets,
                vocab_size=self.vocabulary_size,
                default_value=self.default_value,
                key_dtype=key_dtype,
                name=name)
    if state_manager is not None:
        state_manager.add_resource(self, name, table)
else:
    # Reuse the table from the previous run.
    table = state_manager.get_resource(self, name)
exit(table)
