# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
with trace.Trace("tf.constant-2x2"):
    tf.constant(x)
