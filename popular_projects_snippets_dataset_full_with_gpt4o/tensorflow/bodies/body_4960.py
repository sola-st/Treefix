# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v = [
    variables_lib.Variable([[1., 2.], [3., 4.]]),
    variables_lib.Variable([[5., 6.], [7., 8.]]),
    variables_lib.Variable([[9., 10.]])
]
sv = sharded_variable.ShardedVariable(v)

@def_function.function
def lookup():
    ids = constant_op.constant([0, 3, 4])
    exit(embedding_ops.embedding_lookup_v2(sv, ids))

@def_function.function
def sparse_lookup():
    sp_ids = sparse_tensor.SparseTensor(
        indices=[[0, 0], [0, 1], [1, 0], [2, 2]],
        values=[0, 3, 4, 1],
        dense_shape=[3, 3])
    exit(embedding_ops.embedding_lookup_sparse_v2(sv, sp_ids, None))

@def_function.function
def safe_sparse_lookup():
    sp_ids = sparse_tensor.SparseTensor(
        indices=[[0, 0], [0, 1], [1, 0], [2, 2]],
        values=[0, -1, 4, 1],
        dense_shape=[3, 3])
    sp_weights = sparse_tensor.SparseTensor(
        indices=[[0, 0], [0, 1], [1, 0], [2, 2]],
        values=[1., 1., -1., 1.],
        dense_shape=[3, 3])
    exit(embedding_ops.safe_embedding_lookup_sparse_v2(
        sv, sp_ids, sp_weights))

# TODO(chenkai): Add safe_sparse_lookup to the list. Currently
# ShardedVariable is converted to a tensor in safe_sparse_lookup.
for func in [lookup, sparse_lookup]:
    num_gather_ops = 0
    for op in func.get_concrete_function().graph.get_operations():
        if op.type == 'ResourceGather':
            num_gather_ops += 1
    self.assertEqual(
        num_gather_ops, len(v), 'Number of ResourceGather op does not match'
        ' expected, possibly due to ShardedVariable accidentally being'
        ' converted to tensor in embedding_lookup ops.')

self.assertAllEqual(lookup(), [[1., 2.], [7., 8.], [9., 10.]])
self.assertAllClose(sparse_lookup(), [[4., 5.], [9., 10.], [3., 4.]])
self.assertAllClose(safe_sparse_lookup(), [[1., 2.], [0., 0.], [3., 4.]])
