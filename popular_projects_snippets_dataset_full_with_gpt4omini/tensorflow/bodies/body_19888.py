# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
if weight is not None:
    raise ValueError(
        "Weight specified for dense input {}, which is not allowed. "
        "Weight will always be 1 in this case.".format(path))
# For tensors, there are no indices and no weights.
indices.append(int_zeros)
values.append(math_ops.cast(array_ops.reshape(tensor, [-1]), dtypes.int64))
weights.append(float_zeros)
