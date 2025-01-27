# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get the input shape for the sparse tensor."""
shape = tensor.shape.as_list()
# Only 2 and above rank sparse tensor is supported.
if len(shape) < 2:
    raise ValueError("Only rank 2 and above sparse tensor is supported,"
                     " find rank {} sparse tensor for input {}".format(
                         len(shape), path))
if not feature.output_shape and feature.max_sequence_length > 0:
    # If the max_sequence_length is set and the output shape for FeatureConfig
    # is not set, we modify the shape of the input feature. Only rank 2
    # feature output shape is modified
    if len(shape) == 2:
        # If the sparse tensor is 2D and max_sequence_length is set,
        # we need to add one dimension to the input feature.
        shape.insert(len(shape) - 1, feature.max_sequence_length)

exit(TensorShape(shape))
