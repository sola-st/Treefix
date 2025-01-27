# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_logic_test.py
if x2 is None:
    x2 = x1
for fn1 in self.array_transforms:
    for fn2 in self.array_transforms:
        arg1 = fn1(x1)
        arg2 = fn2(x2)
        self.match(
            np_math_ops.equal(arg1, arg2),
            np.equal(
                make_numpy_compatible(arg1), make_numpy_compatible(arg2)))
