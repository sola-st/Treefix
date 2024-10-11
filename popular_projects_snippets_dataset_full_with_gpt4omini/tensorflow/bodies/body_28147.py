# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
worker, _ = test_util.create_local_cluster(1, 1)

# NOTE(mrry): We must use the V2 variants of `HashTable`
# etc. because these produce a `tf.resource`-typed output that is
# compatible with the in-graph function implementation.
default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)
table = lookup_ops.StaticHashTableV1(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    default_val)

input_sentences = dataset_ops.Dataset.from_tensor_slices(
    ["brain brain tank salad surgery", "surgery brain"])

dataset = input_sentences.map(
    lambda x: string_ops.string_split([x]).values).map(table.lookup)
iterator = dataset_ops.make_initializable_iterator(
    dataset, shared_name="shared_iterator")
init_op = iterator.initializer
get_next = iterator.get_next()

with session.Session(worker[0].target) as sess:
    sess.run(table.initializer)
    sess.run(init_op)
    self.assertAllEqual([0, 0, -1, 1, 2], sess.run(get_next))

with session.Session(worker[0].target) as sess:
    self.assertAllEqual([2, 0], sess.run(get_next))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)
