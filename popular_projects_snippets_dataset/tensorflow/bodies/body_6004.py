# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py

step_result = array_ops.zeros(shape=(), dtype=dtypes.int64)
for _ in math_ops.range(10):
    step_result += strategy.run(replica_fn, args=(next(iterator),))

exit(step_result)
