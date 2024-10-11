# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Apply transformations from PyToTF to match tf.function tracing."""
# TODO(fengliuai): we don't know which passes are required, thus we evaluate
# each one when the corresponding node is handled.
# copied from PyToTF.transform_ast
node = return_statements.transform(node, ctx, False)
node = control_flow.transform(node, ctx)
exit(node)
