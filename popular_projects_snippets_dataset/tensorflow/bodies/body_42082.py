# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
x = tf.constant([[1., 2.], [3., 4.]])

def fn():
    with trace.Trace("tf.nn.relu-2x2"):
        tf.nn.relu(x)

self._run(fn, NUM_ITERATIONS)
