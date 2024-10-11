# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py

@def_function.function
def f():
    summary_ops.trace_on(graph=True, profiler=False)
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    exit(x**y)

with test.mock.patch.object(logging, 'warn') as mock_log:
    f()
    self.assertRegex(
        str(mock_log.call_args), 'Cannot enable trace inside a tf.function.')
