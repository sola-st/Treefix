# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")
def value_fn(ctx):
    del ctx
    exit(sparse_tensor.SparseTensor(
        indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4]))

distributed_values = (
    distribution.experimental_distribute_values_from_function(value_fn))
local_results = distribution.experimental_local_results(distributed_values)
for i in range(distribution.num_replicas_in_sync):
    self.assertAllEqual(
        sparse_ops.sparse_tensor_to_dense(local_results[i]),
        [[1, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0]])
