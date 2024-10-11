# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py

def check(equation, *input_and_placeholder_shapes):
    r = np.random.RandomState(0)
    inputs = []
    input_placeholders = []
    for actual_shape, placeholder_shape in input_and_placeholder_shapes:
        with self.subTest(equation=equation, actual_shape=actual_shape,
                          placeholder_shape=placeholder_shape):
            input_np = np.array(r.randn(*actual_shape))
            inputs.append(input_np)
            input_placeholders.append(
                array_ops.placeholder_with_default(input_np, placeholder_shape))

    a = np.einsum(equation, *inputs)
    b = self.evaluate(gen_linalg_ops.einsum(input_placeholders, equation))
    self.assertAllClose(a, b, atol=1e-4, rtol=1e-4)

check('bijl,bjkm->bik', ((9, 2, 3, 5), (None, None, None, 5)),
      ((9, 3, 4, 7), (None, None, 4, None)))
check('bijl,bjkm->bik', ((9, 2, 3, 5), None), ((9, 3, 4, 7), None))
check('...ij,...->...i', ((4, 3, 1, 2), (None, 3, None, 2)),
      ((4, 3), (None, 3)))
check('...ij,...jk->...ik', ((3, 1, 2, 3), None), ((1, 7, 3, 4), None))
