# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
if self._vocab_size:
    # Keep the shared_name:
    # <table_type>_<filename>_<vocab_size>_<key_index>_<value_index>_<offset>
    if self._offset:
        shared_name = "hash_table_%s_%d_%s_%s_%s" % (
            self._filename_arg, self._vocab_size, self._key_index,
            self._value_index, self._offset)
    else:
        shared_name = "hash_table_%s_%d_%s_%s" % (
            self._filename_arg, self._vocab_size, self._key_index,
            self._value_index)
else:
    # Keep the shared_name
    # <table_type>_<filename>_<key_index>_<value_index>_<offset>
    if self._offset:
        shared_name = "hash_table_%s_%s_%s_%s" % (
            self._filename_arg, self._key_index, self._value_index,
            self._offset)
    else:
        shared_name = "hash_table_%s_%s_%s" % (
            self._filename_arg, self._key_index, self._value_index)

exit(shared_name)
