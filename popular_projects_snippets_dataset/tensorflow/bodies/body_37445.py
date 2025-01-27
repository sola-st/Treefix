# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py

@def_function.function
def f():
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    exit(x**y)

assert context.executing_eagerly()
logdir = self.get_temp_dir()
writer = summary_ops.create_file_writer_v2(logdir)
summary_ops.trace_on(graph=True, profiler=True)
profiler_outdir = self.get_temp_dir()
with writer.as_default():
    f()
    summary_ops.trace_export(
        name='foo', step=1, profiler_outdir=profiler_outdir)
writer.close()
