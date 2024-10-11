# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py

def check(equation, input_shapes, output_shape):
    # All these cases result in an output filled with zeros, so we don't call
    # np.einsum. Also np.einsum doesn't support generalized diagonals which
    # are needed for EinsumOp gradients.
    r = np.random.RandomState(0)
    inputs = [np.array(r.randn(*shape)) for shape in input_shapes]
    output = self.evaluate(gen_linalg_ops.einsum(inputs, equation))
    self.assertAllClose(output, np.zeros(output_shape), atol=1e-4, rtol=1e-4)

# Generalized traces with zero-sized dimensions.
check('aab,bc->ac', [(0, 0, 10), (10, 10)], (0, 10))
check('aaab,bc->c', [(0, 0, 0, 3), (3, 4)], (4,))
# Generalized diagonals along with contraction.
check('ab,bc->aaca', [(0, 10), (10, 5)], (0, 0, 5, 0))
check('ab,bc->aaa', [(0, 10), (10, 5)], (0, 0, 0))
check('ab,bc->cc', [(0, 10), (10, 5)], (5, 5))
check('ab,ab->aaa', [(0, 5), (0, 5)], (0, 0, 0))
