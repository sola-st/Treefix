# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
c = constant_op.constant(1., dtype=dtypes.float32)

def fn():
    exit(gen_math_ops.add(c, 1))

self._run(fn, 10000)
