# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with backprop.GradientTape() as gt:
    gt.watch(m)
    y = f(m, m, transpose_b=transpose_b)
_ = gt.gradient(y, m)
