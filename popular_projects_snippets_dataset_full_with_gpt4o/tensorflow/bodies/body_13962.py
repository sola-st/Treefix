# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/split_benchmark.py
print("Forward vs backward concat")
shapes = [[2000, 8], [8, 2000], [100, 18], [1000, 18], [10000, 18],
          [100, 97], [1000, 97], [10000, 1], [1, 10000]]
axis_ = [1]  # 0 is very fast because it doesn't actually do any copying
num_outputs = 100
variable = [False, True]  # fixed input size or not
for shape in shapes:
    for axis in axis_:
        for v in variable:
            self._run_graph("gpu", shape, v, num_outputs, axis)
