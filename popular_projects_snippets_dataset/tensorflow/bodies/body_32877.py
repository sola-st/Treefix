# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
def check(equation, input_shapes, output_shape):
    # All these cases result in an output filled with zeros, so we don't call
    # np.einsum. Also np.einsum doesn't support generalized diagonals which
    # are needed for EinsumOp gradients.
    r = np.random.RandomState(0)
    inputs = [np.array(r.randn(*shape)) for shape in input_shapes]
    output = self.evaluate(gen_linalg_ops.einsum(inputs, equation))
    self.assertAllClose(output, np.zeros(output_shape), atol=1e-4, rtol=1e-4)

# Contractions along zero-sized dimensions.
check('ab,bc->ac', [(0, 10), (10, 10)], (0, 10))
# From transformer xl.
check('ibnd,ijbn->jnd', [(1, 0, 5, 10), (1, 1, 0, 5)], (1, 5, 10))
