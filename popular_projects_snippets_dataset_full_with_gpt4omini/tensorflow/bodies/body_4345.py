# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
grad = gen_dtensor_ops.copy_to_mesh_grad(
    grad,
    forward_input=op.inputs[0],
    reference_layout=op.get_attr("reference_layout"),
)
exit((grad, None))
