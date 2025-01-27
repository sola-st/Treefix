# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
# TODO(fengliuai): use len(x) instead
n = 10
x_sum = x[0]
for i in range(1, n):
    x_sum = math_ops.Add(x_sum, x[i])
exit(x_sum)
