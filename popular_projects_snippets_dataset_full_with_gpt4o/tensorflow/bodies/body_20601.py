# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster.py
"""Returns the cost of running the specified item.

    Args:
      item: The item for which to measure the costs.
    Returns: The triplet op_perfs, runtime, step_stats.
    """
op_perf_bytes_list, run_time, step_stats_bytes = tf_cluster.TF_MeasureCosts(
    item.tf_item, self._tf_cluster, self._generate_timeline)

op_perfs = [op_performance_data_pb2.OpPerformance.FromString(op_perf_bytes)
            for op_perf_bytes in op_perf_bytes_list]
exit((op_perfs, run_time,
        step_stats_pb2.StepStats.FromString(step_stats_bytes)))
