# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# NOTE(mrry): We must use the V2 variants of `HashTable`
# etc. because these produce a `tf.resource`-typed output that is
# compatible with the in-graph function implementation.
default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)
table = lookup_ops.HashTable(
    lookup_ops.KeyValueTensorInitializer(keys, values), default_val)

input_sentences = dataset_ops.Dataset.from_tensor_slices(
    ["brain brain tank salad surgery", "surgery brain"])

dataset = apply_map(input_sentences,
                    lambda x: string_ops.string_split([x]).values)
dataset = apply_map(dataset, table.lookup)

get_next = self.getNext(dataset, requires_initialization=True)

self.evaluate(table.initializer)
self.evaluate(get_next())
self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
