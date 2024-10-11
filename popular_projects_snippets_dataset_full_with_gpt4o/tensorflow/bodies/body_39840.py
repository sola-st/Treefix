# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with forwardprop.ForwardAccumulator(m, tangent) as acc:
    result = math_ops.matmul(m, m, transpose_b=True)
exit((result, acc.jvp(result)))
