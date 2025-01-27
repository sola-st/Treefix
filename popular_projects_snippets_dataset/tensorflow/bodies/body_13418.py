# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
if self._is_anonymous:
    table_ref = gen_lookup_ops.anonymous_hash_table(
        key_dtype=self._initializer.key_dtype,
        value_dtype=self._initializer.value_dtype,
        name=self._name)
else:
    table_ref = gen_lookup_ops.hash_table_v2(
        shared_name=self._shared_name,
        key_dtype=self._initializer.key_dtype,
        value_dtype=self._initializer.value_dtype,
        name=self._name)
if context.executing_eagerly():
    self._table_name = None
else:
    self._table_name = table_ref.op.name.split("/")[-1]
exit(table_ref)
