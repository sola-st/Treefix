# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
mode = op.get_attr("mode")
exit([gen_array_ops.mirror_pad(grad, op.inputs[1], mode=mode), None])
