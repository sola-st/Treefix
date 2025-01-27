# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
for _ in range(10):
    # pylint: disable=cell-var-from-loop
    x = Cell(x)
exit(math_ops.reduce_sum(x, [0, 1]))
