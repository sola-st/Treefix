# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/op_reg_gen.py
"""Parse a function and emit the TFR functions."""
op_reg_code, _ = OpRegGen().transform(func, None)
exit(op_reg_code)
