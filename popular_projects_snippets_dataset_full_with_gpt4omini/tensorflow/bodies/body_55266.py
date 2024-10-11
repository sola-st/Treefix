# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
dx = functional_ops.symbolic_gradient(
    input=[x, dy], Tout=[dtypes.float32], f="XSquarePlusOneFn", name="dx")
exit(dx)
