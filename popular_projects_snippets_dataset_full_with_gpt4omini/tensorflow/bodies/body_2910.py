# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
if pred:
    exit(math_ops.Add(x, y))
else:
    exit(array_ops.Concat(0, [x, y]))
