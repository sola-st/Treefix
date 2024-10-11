# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
"""Run a random test case with the given shape and indices.

    Args:
      shape: Shape of the parameters array.
      indices: One-dimensional array of ints, the indices of the last dimension
               of the parameters to update.
      scatter_op: ScatterAdd or ScatterSub.
    """
super(ScatterAddSubTest, self).setUp()
with self.cached_session(use_gpu=False):
    # Create a random parameter array of given shape
    p_init = np.random.rand(*shape).astype("f")
    # Create the shape of the update array. All dimensions except the last
    # match the parameter array, the last dimension equals the # of indices.
    vals_shape = [len(indices)] + shape[1:]
    vals_init = np.random.rand(*vals_shape).astype("f")
    v_i = [float(x) for x in vals_init.ravel()]
    p = variables.Variable(p_init)
    vals = constant_op.constant(v_i, shape=vals_shape, name="vals")
    ind = constant_op.constant(indices, dtype=dtypes.int32)
    p2 = scatter_op(p, ind, vals, name="updated_p")
    # p = init
    self.evaluate(variables.global_variables_initializer())
    # p += vals
    result = self.evaluate(p2)
# Compute the expected 'p' using numpy operations.
for i, ind in enumerate(indices):
    if scatter_op == state_ops.scatter_add:
        p_init.reshape(shape[0], -1)[ind, :] += (vals_init.reshape(
            vals_shape[0], -1)[i, :])
    else:
        p_init.reshape(shape[0], -1)[ind, :] -= (vals_init.reshape(
            vals_shape[0], -1)[i, :])
self.assertTrue(all((p_init == result).ravel()))
