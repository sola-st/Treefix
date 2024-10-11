# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
x_np = [[[[1, 10], [2, 20], [5, 50], [6, 60]],
         [[3, 30], [4, 40], [7, 70], [8, 80]],
         [[9, 90], [10, 100], [13, 130], [14, 140]],
         [[11, 110], [12, 120], [15, 150], [16, 160]]]]
block_size = 2
x_out = [[[[1, 10, 2, 20, 3, 30, 4, 40], [5, 50, 6, 60, 7, 70, 8, 80]],
          [[9, 90, 10, 100, 11, 110, 12, 120],
           [13, 130, 14, 140, 15, 150, 16, 160]]]]
self._testOne(x_np, block_size, x_out)
