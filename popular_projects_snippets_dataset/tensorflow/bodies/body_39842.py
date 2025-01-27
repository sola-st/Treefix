# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with forwardprop.ForwardAccumulator(x, tangent) as acc:
    result = math_ops.matmul(x, x, transpose_b=True)
exit((result, acc.jvp(result)))
