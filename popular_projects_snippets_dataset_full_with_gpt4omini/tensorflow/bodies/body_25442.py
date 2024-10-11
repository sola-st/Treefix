# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
options = config_pb2.RunOptions()
options.trace_level = config_pb2.RunOptions.FULL_TRACE
run_metadata = config_pb2.RunMetadata()

with session.Session(config=no_rewrite_session_config()) as sess:
    a = constant_op.constant([1, 2, 3])
    b = constant_op.constant([2, 2, 1])
    result = math_ops.add(a, b)

    sess.run(result, options=options, run_metadata=run_metadata)

    prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(
        sess.graph, run_metadata)
    prof_output = prof_analyzer.list_profile([]).lines

    _assert_at_least_one_line_matches("Device 1 of", prof_output)
    expected_headers = [
        "Node", r"Start Time \(us\)", r"Op Time \(.*\)", r"Exec Time \(.*\)",
        r"Filename:Lineno\(function\)"]
    _assert_at_least_one_line_matches(
        ".*".join(expected_headers), prof_output)
    _assert_at_least_one_line_matches(r"^Add/", prof_output)
    _assert_at_least_one_line_matches(r"Device Total", prof_output)
