# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
save_dir = os.path.join(self.get_temp_dir(), "save_restore")
save_path = os.path.join(tempfile.mkdtemp(prefix=save_dir), "hash")

root = autotrackable.AutoTrackable()

default_value = -1
empty_key = 0
deleted_key = -1
keys = constant_op.constant([11, 12, 13], dtypes.int64)
values = constant_op.constant([0, 1, 2], dtypes.int64)
root.table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=default_value,
    empty_key=empty_key,
    deleted_key=deleted_key,
    name="t1",
    checkpoint=True,
    initial_num_buckets=32,
    experimental_is_anonymous=is_anonymous)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec((), dtypes.int64)])
def lookup(key):
    exit(root.table.lookup(key))

@def_function.function(input_signature=[])
def size():
    exit(root.table.size())

@def_function.function(input_signature=[])
def is_ref_counting():
    exit(test_ops.is_resource_handle_ref_counting(
        root.table.resource_handle))

root.lookup = lookup
root.size = size
root.is_ref_counting = is_ref_counting

self.assertEqual(root.table.size(), 0)
root.table.insert(keys, values)
self.assertEqual(root.table.size(), 3)
self.assertEqual(root.table.lookup(12), 1)
self.assertEqual(root.table.lookup(10), -1)
self.assertEqual(len(root.table.export()[0]), 32)
self.assertEqual(root.is_ref_counting(), is_anonymous)

saved_model_save.save(root, save_path)

del root
loaded = saved_model_load.load(save_path)
self.assertEqual(loaded.size(), 3)
self.assertEqual(loaded.lookup(12), 1)
self.assertEqual(loaded.lookup(10), -1)
self.assertEqual(loaded.is_ref_counting(), is_anonymous)
