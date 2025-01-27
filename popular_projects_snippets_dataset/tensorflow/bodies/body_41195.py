# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
# begin is a compile-time constant, even if x is not
begin = array_ops.shape_v2(x)[0] - 2
exit(x[begin:])
