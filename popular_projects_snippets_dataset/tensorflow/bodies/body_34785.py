# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("feat_to_id_7.txt")
input_indices = [[0, 0], [0, 1], [2, 0], [2, 2], [3, 0]]
input_shape = [4, 4]
sp_features = sparse_tensor.SparseTensor(
    constant_op.constant(input_indices, dtypes.int64),
    constant_op.constant(["brain", "salad", "brain", "surgery", "tarkus"],
                         dtypes.string),
    constant_op.constant(input_shape, dtypes.int64))

table = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(vocab_file, vocab_size=3),
        -1), 1)
self.evaluate(table.initializer)

sp_ids = table.lookup(sp_features)

self.assertAllEqual([5], sp_ids.values._shape_as_list())

sp_ids_ind, sp_ids_val, sp_ids_shape = self.evaluate(
    [sp_ids.indices, sp_ids.values, sp_ids.dense_shape])

self.assertAllEqual(input_indices, sp_ids_ind)
self.assertAllEqual([0, 1, 0, 2, 3], sp_ids_val)
self.assertAllEqual(input_shape, sp_ids_shape)
