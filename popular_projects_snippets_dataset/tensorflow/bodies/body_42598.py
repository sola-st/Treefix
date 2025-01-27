# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test_base.py
if enable_python_trace:
    options = profiler.ProfilerOptions(python_tracer_level=1)
    logdir = os.path.join(flags.FLAGS.logdir, suid + "_with_python")
else:
    options = profiler.ProfilerOptions(python_tracer_level=0)
    logdir = os.path.join(flags.FLAGS.logdir, suid)
with profiler.Profile(logdir, options):
    total_time = run_benchmark(func, num_iters_xprof, execution_mode)
us_per_example = float("{0:.3f}".format(total_time * 1e6 / num_iters_xprof))
exit((logdir, us_per_example))
