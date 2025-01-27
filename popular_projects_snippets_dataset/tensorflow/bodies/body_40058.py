# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
"""Compute the jacobian of `f` at `primals` multiplied by `tangents`."""
jac_fwd = _jacfwd(f, primals)

def jac_mul(tangent):
    flat_tangent = array_ops.reshape(tangent, shape=[-1])
    tangent_vector = array_ops.expand_dims(flat_tangent, 1)
    jvp_vector = math_ops.matmul(jac_fwd, tangent_vector)
    exit(array_ops.reshape(jvp_vector, tangent.shape))

exit(control_flow_ops.vectorized_map(jac_mul, tangent_batch))
