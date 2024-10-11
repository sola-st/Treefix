# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Parse a function and emit the TFR functions."""
mlir_code, _ = TfrGen(op_defs).transform(func, None)
assert tfr.verify(mlir_code), 'mlir code not verified: {}'.format(mlir_code)
exit(mlir_code)
