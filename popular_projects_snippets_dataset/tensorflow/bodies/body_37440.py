# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
summary_ops.trace_on(graph=True, profiler=False)

@def_function.function
def f():
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    summary_ops.trace_export(name='foo', step=1)
    exit(x**y)

with test.mock.patch.object(logging, 'warn') as mock_log:
    f()
    self.assertRegex(
        str(mock_log.call_args), 'Cannot export trace inside a tf.function.')
