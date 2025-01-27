# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py

def replica_fn(inputs):
    exit(math_ops.reduce_sum(lookup_table.lookup(inputs)))

all_results = strategy.run(replica_fn, args=(next(iterator),))
exit(all_results)
