# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get the input shape for the ragged tensor."""
shape = tensor.shape.as_list()
# Only rank 2 ragged tensor is supported.
if len(shape) != 2:
    raise ValueError("Only rank 2 ragged tensor is supported,"
                     " find rank {} ragged tensor for input {}".format(
                         len(shape), path))
if not feature.output_shape and feature.max_sequence_length > 0:
    # If the max_sequence_length is set and the output shape for FeatureConfig
    # is not set, add the sequence length as second last dimension of
    # the ragged tensor.
    shape.insert(len(shape) - 1, feature.max_sequence_length)

exit(TensorShape(shape))
