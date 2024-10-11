# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
depth_radius = op.get_attr("depth_radius")
bias = op.get_attr("bias")
alpha = op.get_attr("alpha")
beta = op.get_attr("beta")
exit([
    gen_nn_ops.lrn_grad(grad, op.inputs[0], op.outputs[0], depth_radius, bias,
                        alpha, beta)
])
