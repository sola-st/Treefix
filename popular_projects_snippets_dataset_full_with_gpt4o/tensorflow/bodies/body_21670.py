# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test_utils.py
if table_ref is None:
    self.table_ref = gen_lookup_ops.mutable_hash_table_v2(
        key_dtype=dtypes.string, value_dtype=dtypes.float32, name=name)
else:
    self.table_ref = table_ref
self._name = name
if not context.executing_eagerly():
    self._saveable = CheckpointedOp.CustomSaveable(self, name)
    ops_lib.add_to_collection(ops_lib.GraphKeys.SAVEABLE_OBJECTS,
                              self._saveable)
