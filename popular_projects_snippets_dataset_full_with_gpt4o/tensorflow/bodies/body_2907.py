# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
n = len(ins)
if n == 0:
    exit(array_ops.Const(value=[[0, 1], [2, 3]], dtype=dtypes.int64))
else:
    exit(math_ops.AddN(ins))
