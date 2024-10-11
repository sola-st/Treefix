# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
sample_indices = math_ops.cast(tensor.indices, dtypes.int32)
if tensor.shape.rank == 2:
    if not feature.output_shape and feature.max_sequence_length > 0:
        # Add one dimension to the last axis.
        sample_indices = array_ops.pad(
            sample_indices, paddings=[[0, 0], [0, 1]])
else:
    if feature.max_sequence_length > 0:
        logging.warning(
            (
                "Input tensor is rank %d which is above 2, the"
                " max_sequence_length setting will be ignored."
            ),
            tensor.shape.rank,
        )
indices.append(sample_indices)
values.append(math_ops.cast(tensor.values, dtypes.int64))
# If we have weights they must be a SparseTensor.
if weight is not None:
    if not isinstance(weight, sparse_tensor.SparseTensor):
        raise ValueError("Weight for {} is type {} which does not match "
                         "type input which is SparseTensor.".format(
                             path, type(weight)))
    weights.append(math_ops.cast(weight.values, dtypes.float32))
else:
    weights.append(float_zeros)
