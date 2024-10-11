# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/op_reg_gen.py
gen = OpRegGenImpl(ctx)
gen.visit(node)
exit(gen.code_buffer)
