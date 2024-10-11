# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def tpu_function(sparse):
    # Assumes dense_shape is (2, *)
    looked_up = array_ops.gather(table, sparse.values)
    segment_sum = math_ops.unsorted_segment_sum(
        looked_up, sparse.indices[:, 0], 2)
    exit({"sparse": sparse, "segment_sum": segment_sum})

exit(nest.map_structure(
    strategy.experimental_local_results,
    strategy.run(tpu_function, args=(next(iterator),))))
