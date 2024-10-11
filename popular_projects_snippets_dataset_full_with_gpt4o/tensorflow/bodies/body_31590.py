# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
"""Iterator for some of the max pool ops in the Inception 2015 model.

  Args:
    shrink: Factor to shrink depth relative to Inception.

  Yields:
    Tuple (name, input_size, filter_size, out_size, strides, padding)
  """
names = ["maxpool2", "maxpool3", "maxpool4", "maxpool5"]
input_sizes = [[32, 71, 71, 192], [32, 35, 35, 288], [32, 17, 17, 1248],
               [32, 8, 8, 2048]]
filter_sizes = [[1, 3, 3, 1], [1, 3, 3, 1], [1, 3, 3, 1], [1, 3, 3, 1]]
output_sizes = [[32, 35, 35, 192], [32, 17, 17, 288], [32, 8, 8, 1248],
                [32, 8, 8, 2048]]
strides = [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]
# Shrink each depth value
for i in input_sizes:
    i[3] //= shrink
for o in output_sizes:
    o[3] //= shrink
paddings = ["VALID", "VALID", "VALID", "SAME"]
for n, i, f, o, s, p in zip(names, input_sizes, filter_sizes, output_sizes,
                            strides, paddings):
    exit((n, i, f, o, s, p))
