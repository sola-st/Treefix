# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
product = self.operators[0].to_dense()
for operator in self.operators[1:]:
    # Product has shape [B, R1, 1, C1, 1].
    product = product[
        ..., :, array_ops.newaxis, :, array_ops.newaxis]
    # Operator has shape [B, 1, R2, 1, C2].
    op_to_mul = operator.to_dense()[
        ..., array_ops.newaxis, :, array_ops.newaxis, :]
    # This is now [B, R1, R2, C1, C2].
    product = product * op_to_mul
    # Now merge together dimensions to get [B, R1 * R2, C1 * C2].
    product_shape = _prefer_static_shape(product)
    shape = _prefer_static_concat_shape(
        product_shape[:-4],
        [product_shape[-4] * product_shape[-3],
         product_shape[-2] * product_shape[-1]])

    product = array_ops.reshape(product, shape=shape)
product.set_shape(self.shape)
exit(product)
