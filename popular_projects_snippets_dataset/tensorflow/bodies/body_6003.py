# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
replica_result = array_ops.zeros(shape=(), dtype=dtypes.int64)
for _ in math_ops.range(10):
    replica_result += math_ops.reduce_sum(model.use_table(batch_data))
exit(replica_result)
