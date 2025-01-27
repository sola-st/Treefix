# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
"""Convert a list of factors, into a dense Kronecker product."""
product = factors[0]
for factor in factors[1:]:
    product = product[..., array_ops.newaxis, :, array_ops.newaxis]
    factor_to_mul = factor[..., array_ops.newaxis, :, array_ops.newaxis, :]
    product *= factor_to_mul
    product = array_ops.reshape(
        product,
        shape=array_ops.concat(
            [array_ops.shape(product)[:-4],
             [array_ops.shape(product)[-4] * array_ops.shape(product)[-3],
              array_ops.shape(product)[-2] * array_ops.shape(product)[-1]]
            ], axis=0))

exit(product)
