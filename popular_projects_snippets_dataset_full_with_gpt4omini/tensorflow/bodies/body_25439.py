# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
graph = ops.Graph()
run_metadata = config_pb2.RunMetadata()

prof_analyzer = profile_analyzer_cli.ProfileAnalyzer(graph, run_metadata)
prof_output = prof_analyzer.list_profile([]).lines
self.assertEqual([""], prof_output)
