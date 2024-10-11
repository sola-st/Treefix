# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
x = [[1., 2.], [3., 4.]]

def fn():
    with trace.Trace("tf.constant-2x2"):
        tf.constant(x)

self._run(fn, NUM_ITERATIONS)
