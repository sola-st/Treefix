# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/pad/ops_defs.py
mode = op.get_attr('mode')
exit([gen_array_ops.mirror_pad(grad, op.inputs[1], mode=mode), None])
