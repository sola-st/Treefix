# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/concat_benchmark.py
print("Forward vs backward concat")
shapes = [[2000, 8], [8, 2000], [100, 18], [1000, 18], [100, 97],
          [1000, 97], [10000, 1], [1, 10000]]
axis_ = [0, 1]
num_inputs = 20
num_iters = [10] * len(shapes)
variable = [False, True]  # fixed input size or not
for shape, iters in zip(shapes, num_iters):
    for axis in axis_:
        for v in variable:
            self._run_graph("cpu", shape, v, num_inputs, axis, True, iters)
