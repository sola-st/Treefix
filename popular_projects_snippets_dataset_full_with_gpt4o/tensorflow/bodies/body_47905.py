# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if inputs.dtype.base_dtype != self._compute_dtype_object.base_dtype:
    inputs = math_ops.cast(inputs, dtype=self._compute_dtype_object)

rank = inputs.shape.rank
if rank == 2 or rank is None:
    # We use embedding_lookup_sparse as a more efficient matmul operation for
    # large sparse input tensors. The op will result in a sparse gradient, as
    # opposed to sparse_ops.sparse_tensor_dense_matmul which results in dense
    # gradients. This can lead to sigfinicant speedups, see b/171762937.
    if isinstance(inputs, sparse_tensor.SparseTensor):
        # We need to fill empty rows, as the op assumes at least one id per row.
        inputs, _ = sparse_ops.sparse_fill_empty_rows(inputs, 0)
        # We need to do some munging of our input to use the embedding lookup as
        # a matrix multiply. We split our input matrix into separate ids and
        # weights tensors. The values of the ids tensor should be the column
        # indices of our input matrix and the values of the weights tensor
        # can continue to the actual matrix weights.
        # The column arrangement of ids and weights
        # will be summed over and does not matter. See the documentation for
        # sparse_ops.sparse_tensor_dense_matmul a more detailed explanation
        # of the inputs to both ops.
        ids = sparse_tensor.SparseTensor(
            indices=inputs.indices,
            values=inputs.indices[:, 1],
            dense_shape=inputs.dense_shape)
        weights = inputs
        outputs = embedding_ops.embedding_lookup_sparse_v2(
            self.kernel, ids, weights, combiner='sum')
    else:
        outputs = gen_math_ops.MatMul(a=inputs, b=self.kernel)
    # Broadcast kernel to inputs.
else:
    outputs = standard_ops.tensordot(inputs, self.kernel, [[rank - 1], [0]])
    # Reshape the output back to the original ndim of the input.
    if not context.executing_eagerly():
        shape = inputs.shape.as_list()
        output_shape = shape[:-1] + [self.kernel.shape[-1]]
        outputs.set_shape(output_shape)

if self.use_bias:
    outputs = nn_ops.bias_add(outputs, self.bias)

if self.activation is not None:
    outputs = self.activation(outputs)
exit(outputs)
