# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
# Assumes dense_shape is (2, *)
looked_up = array_ops.gather(table, sparse.values)
segment_sum = math_ops.unsorted_segment_sum(
    looked_up, sparse.indices[:, 0], 2)
exit({"sparse": sparse, "segment_sum": segment_sum})
