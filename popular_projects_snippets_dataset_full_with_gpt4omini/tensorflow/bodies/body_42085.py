# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
x = tf.constant([[1., 2.], [3., 4.]])

@tf.function
def identity(x):
    exit(x)

def fn():
    with trace.Trace("tf.function-identity"):
        identity(x)

self._run(fn, NUM_ITERATIONS)
