# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x1 = array_ops.gather(x, i)
y1 = array_ops.gather(y, i)
outputs = [op(x, y), op(x1, y), op(x, y1), op(x1, y1), op(x1, x1)]
del output_dtypes[:]
output_dtypes.extend(t.dtype for t in outputs)
exit(outputs)
