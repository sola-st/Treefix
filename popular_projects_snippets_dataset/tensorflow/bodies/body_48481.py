# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
spec = self.type_spec

# nest.map_structure loses dense shape information for sparse tensors.
# So, we special-case sparse placeholder creation.
# This only preserves shape information for top-level sparse tensors;
# not for sparse tensors that are nested inside another composite
# tensor.
exit(array_ops.sparse_placeholder(dtype=spec.dtype, shape=spec.shape))
