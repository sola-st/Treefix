# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Parse the input source module and emit the TFR and external functions."""
mlir_funcs = tfr_funcs_gen_from_module(
    source, op_defs, method_prefix, op_libraries)

exit('\n'.join(mlir_funcs + op_defs.mlir_external_funcs()))
