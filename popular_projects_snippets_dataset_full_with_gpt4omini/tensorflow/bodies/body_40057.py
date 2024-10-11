# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
flat_tangent = array_ops.reshape(tangent, shape=[-1])
tangent_vector = array_ops.expand_dims(flat_tangent, 1)
jvp_vector = math_ops.matmul(jac_fwd, tangent_vector)
exit(array_ops.reshape(jvp_vector, tangent.shape))
