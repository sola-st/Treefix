# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with test.mock.patch.object(logging, 'warn') as mock_log:
    with context.graph_mode():
        summary_ops.trace_on(graph=True, profiler=False)
    self.assertRegex(
        str(mock_log.call_args), 'Must enable trace in eager mode.')
