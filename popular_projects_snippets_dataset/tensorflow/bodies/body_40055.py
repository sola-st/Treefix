# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
"""Compute the jacobian of `f` at `primals` using forward-mode autodiff."""
jac_flat = []
flat_primals = nest.flatten(primals)
tangent_mask = [
    array_ops.zeros_like(primal, dtype=primal.dtype)
    for primal in flat_primals
]
for primal_index, primal in enumerate(flat_primals):
    primal_vector = array_ops.reshape(primal, [-1])
    primal_vector_length = array_ops.size(primal_vector)
    jac_columns = []
    for element_index in math_ops.range(primal_vector_length):
        mask = array_ops.one_hot(
            element_index, primal_vector_length, dtype=primal.dtype)
        tangent_mask[primal_index] = array_ops.reshape(mask,
                                                       array_ops.shape(primal))
        jac_columns.append(
            nest.map_structure(
                functools.partial(array_ops.reshape, shape=[-1]),
                _jvp(f, primals, nest.pack_sequence_as(primals,
                                                       tangent_mask))[1]))
    jac_flat.append(array_ops.stack(jac_columns, axis=1))
    tangent_mask[primal_index] = array_ops.zeros_like(primal)
exit(nest.pack_sequence_as(primals, jac_flat))
