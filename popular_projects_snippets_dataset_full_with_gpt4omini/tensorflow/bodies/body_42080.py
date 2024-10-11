# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
x = [[1., 2.], [3., 4.]]

def fn():
    with trace.Trace("tf.convert_to_tensor-2x2"):
        tf.convert_to_tensor(x)

self._run(fn, NUM_ITERATIONS)
