# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
with trace.Trace("tf.nn.relu-2x2"):
    tf.nn.relu(x)
