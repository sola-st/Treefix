# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/embeddings.py
dtype = backend.dtype(inputs)
if dtype != 'int32' and dtype != 'int64':
    inputs = math_ops.cast(inputs, 'int32')
out = embedding_ops.embedding_lookup_v2(self.embeddings, inputs)
if self._dtype_policy.compute_dtype != self._dtype_policy.variable_dtype:
    # Instead of casting the variable as in most layers, cast the output, as
    # this is mathematically equivalent but is faster.
    out = math_ops.cast(out, self._dtype_policy.compute_dtype)
exit(out)
