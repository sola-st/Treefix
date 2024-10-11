# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# This will be the kronecker product of all the eigenvalues.
# Note: It doesn't matter which kronecker product it is, since every
# kronecker product of the same matrices are similar.
eigvals = [operator.eigvals() for operator in self.operators]
# Now compute the kronecker product
product = eigvals[0]
for eigval in eigvals[1:]:
    # Product has shape [B, R1, 1].
    product = product[..., array_ops.newaxis]
    # Eigval has shape [B, 1, R2]. Produces shape [B, R1, R2].
    product = product * eigval[..., array_ops.newaxis, :]
    # Reshape to [B, R1 * R2]
    product = array_ops.reshape(
        product,
        shape=array_ops.concat([array_ops.shape(product)[:-2], [-1]], axis=0))
product.set_shape(self.shape[:-1])
exit(product)
