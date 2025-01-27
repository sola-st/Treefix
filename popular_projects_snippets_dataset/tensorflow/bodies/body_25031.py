# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/profiling_test.py
node_1 = step_stats_pb2.NodeExecStats(
    node_name="Add/123",
    op_start_rel_micros=3,
    op_end_rel_micros=5,
    all_end_rel_micros=4)
self.profile_datum_1 = profiling.ProfileDatum(
    "cpu:0", node_1, "/foo/bar.py", 10, "func1", "Add")

node_2 = step_stats_pb2.NodeExecStats(
    node_name="Mul/456",
    op_start_rel_micros=13,
    op_end_rel_micros=16,
    all_end_rel_micros=17)
self.profile_datum_2 = profiling.ProfileDatum(
    "cpu:0", node_2, "/foo/bar.py", 11, "func1", "Mul")

node_3 = step_stats_pb2.NodeExecStats(
    node_name="Add/123",
    op_start_rel_micros=103,
    op_end_rel_micros=105,
    all_end_rel_micros=4)
self.profile_datum_3 = profiling.ProfileDatum(
    "cpu:0", node_3, "/foo/bar.py", 12, "func1", "Add")

node_4 = step_stats_pb2.NodeExecStats(
    node_name="Add/123",
    op_start_rel_micros=203,
    op_end_rel_micros=205,
    all_end_rel_micros=4)
self.profile_datum_4 = profiling.ProfileDatum(
    "gpu:0", node_4, "/foo/bar.py", 13, "func1", "Add")
