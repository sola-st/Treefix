# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_building_benchmark.py
with context.execution_mode(context.GRAPH_MODE):
    x = array_ops.placeholder(
        shape=[784, 1000], dtype=dtypes.float32, name="x")
    y = array_ops.placeholder(
        shape=[1000, 1000], dtype=dtypes.float32, name="y")

    def bench():
        exit(gen_math_ops.mat_mul(x, y))

    self._run_and_report(bench, 1000)
