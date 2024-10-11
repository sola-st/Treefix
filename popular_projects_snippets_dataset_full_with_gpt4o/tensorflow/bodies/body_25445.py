# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
node1 = step_stats_pb2.NodeExecStats(
    node_name="Add/123",
    all_start_micros=123,
    op_start_rel_micros=3,
    op_end_rel_micros=5,
    all_end_rel_micros=4)

node2 = step_stats_pb2.NodeExecStats(
    node_name="Mul/456",
    all_start_micros=122,
    op_start_rel_micros=1,
    op_end_rel_micros=2,
    all_end_rel_micros=5)

run_metadata = config_pb2.RunMetadata()
device1 = run_metadata.step_stats.dev_stats.add()
device1.device = "deviceA"
device1.node_stats.extend([node1, node2])

graph = test.mock.MagicMock()
op1 = test.mock.MagicMock()
op1.name = "Add/123"
op1.traceback = [("a/b/file2", 10, "some_var")]
op1.type = "add"
op2 = test.mock.MagicMock()
op2.name = "Mul/456"
op2.traceback = [("a/b/file1", 11, "some_var")]
op2.type = "mul"
graph.get_operations.return_value = [op1, op2]

prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(graph, run_metadata)

# Force time unit.
prof_output = prof_analyzer.list_profile(["--time_unit", "ms"]).lines
_assert_at_least_one_line_matches(r"Add/123.*add.*0\.002ms", prof_output)
_assert_at_least_one_line_matches(r"Mul/456.*mul.*0\.005ms", prof_output)
_assert_at_least_one_line_matches(r"Device Total.*0\.009ms", prof_output)
