# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
with trace.Trace("tf.convert_to_tensor-2x2"):
    tf.convert_to_tensor(x)
