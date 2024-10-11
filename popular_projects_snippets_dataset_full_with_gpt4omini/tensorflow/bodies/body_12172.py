# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py

def check(equation, input_shapes, output_shape):
    # All these cases result in an output filled with zeros, so we don't call
    # np.einsum. Also np.einsum doesn't support generalized diagonals which
    # are needed for EinsumOp gradients.
    r = np.random.RandomState(0)
    inputs = [np.array(r.randn(*shape)) for shape in input_shapes]
    input_tensors = [constant_op.constant(x, shape=x.shape) for x in inputs]
    output = self.evaluate(special_math_ops.einsum(equation, *input_tensors))
    self.assertAllClose(output, np.zeros(output_shape), atol=1e-4, rtol=1e-4)

# Contractions along zero-sized dimensions.
check('ab,bc->ac', [(0, 10), (10, 10)], (0, 10))
# From transformer xl.
check('ibnd,ijbn->jnd', [(1, 0, 5, 10), (1, 1, 0, 5)], (1, 5, 10))

# Generalized traces with zero-sized dimensions.
check('aab,bc->ac', [(0, 0, 10), (10, 10)], (0, 10))
check('aaab,bc->c', [(0, 0, 0, 3), (3, 4)], (4,))
