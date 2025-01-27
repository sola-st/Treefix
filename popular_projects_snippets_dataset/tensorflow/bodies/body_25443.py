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

# Default sort by start time (i.e. all_start_micros).
prof_output = prof_analyzer.list_profile([]).lines
self.assertRegex("".join(prof_output), r"Mul/456.*Add/123")
# Default sort in reverse.
prof_output = prof_analyzer.list_profile(["-r"]).lines
self.assertRegex("".join(prof_output), r"Add/123.*Mul/456")
# Sort by name.
prof_output = prof_analyzer.list_profile(["-s", "node"]).lines
self.assertRegex("".join(prof_output), r"Add/123.*Mul/456")
# Sort by op time (i.e. op_end_rel_micros - op_start_rel_micros).
prof_output = prof_analyzer.list_profile(["-s", "op_time"]).lines
self.assertRegex("".join(prof_output), r"Mul/456.*Add/123")
# Sort by exec time (i.e. all_end_rel_micros).
prof_output = prof_analyzer.list_profile(["-s", "exec_time"]).lines
self.assertRegex("".join(prof_output), r"Add/123.*Mul/456")
# Sort by line number.
prof_output = prof_analyzer.list_profile(["-s", "line"]).lines
self.assertRegex("".join(prof_output), r"Mul/456.*Add/123")
