# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
block_size = 2
def batch_input_elt(i):
    exit([[[1 * i, 2 * i, 3 * i, 4 * i],
             [5 * i, 6 * i, 7 * i, 8 * i]],
            [[9 * i, 10 * i, 11 * i, 12 * i],
             [13 * i, 14 * i, 15 * i, 16 * i]]])
def batch_output_elt(i):
    exit([[[1 * i], [2 * i], [5 * i], [6 * i]],
            [[3 * i], [4 * i], [7 * i], [8 * i]],
            [[9 * i], [10 * i], [13 * i], [14 * i]],
            [[11 * i], [12 * i], [15 * i], [16 * i]]])
batch_size = 10
x_np = [batch_input_elt(i) for i in range(batch_size)]
x_out = [batch_output_elt(i) for i in range(batch_size)]
self._testOne(x_np, block_size, x_out)
