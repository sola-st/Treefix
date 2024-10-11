# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not context.executing_eagerly():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
save_dir = os.path.join(self.get_temp_dir(), "save_restore")
save_prefix = os.path.join(tempfile.mkdtemp(prefix=save_dir), "hash")

default_value = -1
empty_key = 0
deleted_key = -1
keys = constant_op.constant([11, 12, 13], dtypes.int64)
values = constant_op.constant([0, 1, 2], dtypes.int64)
save_table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=default_value,
    empty_key=empty_key,
    deleted_key=deleted_key,
    name="t1",
    checkpoint=True,
    initial_num_buckets=32,
    experimental_is_anonymous=is_anonymous)

save_checkpoint = trackable.Checkpoint(table=save_table)

self.assertAllEqual(0, self.evaluate(save_table.size()))
self.evaluate(save_table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(save_table.size()))
self.assertAllEqual(32, len(self.evaluate(save_table.export()[0])))

save_path = save_checkpoint.save(save_prefix)
del save_table, save_checkpoint

load_table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=default_value,
    empty_key=empty_key,
    deleted_key=deleted_key,
    name="t1",
    checkpoint=True,
    initial_num_buckets=64,
    experimental_is_anonymous=is_anonymous)
self.evaluate(
    load_table.insert(
        constant_op.constant([11, 14], dtypes.int64),
        constant_op.constant([12, 24], dtypes.int64)))
self.assertAllEqual(2, self.evaluate(load_table.size()))
self.assertAllEqual(64, len(self.evaluate(load_table.export()[0])))

restore_checkpoint = trackable.Checkpoint(table=load_table)

# Restore the saved values in the parameter nodes.
restore_checkpoint.restore(save_path).run_restore_ops()

self.assertAllEqual(3, self.evaluate(load_table.size()))
self.assertAllEqual(32, len(self.evaluate(load_table.export()[0])))

input_string = constant_op.constant([10, 11, 12, 13, 14], dtypes.int64)
output = load_table.lookup(input_string)
self.assertAllEqual([-1, 0, 1, 2, -1], self.evaluate(output))
