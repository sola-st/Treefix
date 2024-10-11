# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
with trace.Trace("tf.function-identity"):
    identity(x)
