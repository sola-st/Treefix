# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
node1 = step_stats_pb2.NodeExecStats(
    node_name="Add/123",
    op_start_rel_micros=3,
    op_end_rel_micros=5,
    all_end_rel_micros=3)

run_metadata = config_pb2.RunMetadata()
device1 = run_metadata.step_stats.dev_stats.add()
device1.device = "deviceA"
device1.node_stats.extend([node1])

device2 = run_metadata.step_stats.dev_stats.add()
device2.device = "deviceB"
device2.node_stats.extend([node1])

graph = test.mock.MagicMock()
op = test.mock.MagicMock()
op.name = "Add/123"
op.traceback = [("a/b/file1", 10, "some_var")]
op.type = "abc"
graph.get_operations.return_value = [op]

prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(graph, run_metadata)
prof_output = prof_analyzer.list_profile([]).lines

_assert_at_least_one_line_matches(r"Device 1 of 2: deviceA", prof_output)
_assert_at_least_one_line_matches(r"Device 2 of 2: deviceB", prof_output)

# Try filtering by device.
prof_output = prof_analyzer.list_profile(["-d", "deviceB"]).lines
_assert_at_least_one_line_matches(r"Device 2 of 2: deviceB", prof_output)
_assert_no_lines_match(r"Device 1 of 2: deviceA", prof_output)
