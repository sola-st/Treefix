# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get and update the per replica output shapes from the input."""
per_replica_output_shapes = None
if per_replica_batch_size and per_replica_input_shapes is None:
    logging.warning(
        "per_replica_batch_size argument will be deprecated, please specify "
        "all the input shapes using per_replica_input_shapes argument.")
    per_replica_output_shapes = self._get_output_shapes_from_batch_size(
        per_replica_batch_size)

# Update the input shapes if provided.
if per_replica_input_shapes is not None:
    if isinstance(per_replica_input_shapes, int):
        logging.warning(
            "Passing batch size to per_replica_input_shapes argument will be"
            " deprecated, please specify all the input shapes using"
            " per_replica_input_shapes argument.")
        per_replica_output_shapes = self._get_output_shapes_from_batch_size(
            per_replica_input_shapes)
    else:
        nest.assert_same_structure(
            nest.flatten(per_replica_input_shapes),
            nest.flatten(self._feature_config))

        # Convert the nested structure to list.
        per_replica_input_shapes = nest.flatten(per_replica_input_shapes)

        per_replica_output_shapes = self._get_output_shapes_from_input_shapes(
            per_replica_input_shapes)

if per_replica_output_shapes is not None:

    # Check the output shapes with existing output shapes setting.
    self._check_output_shapes(per_replica_output_shapes)

    # Update the output shapes with existing output shapes setting.
    # This is necessary Because the output shapes might be missing from
    # the feature config, the usr can set it:
    #  1. calling the build method
    #  2. output shapes auto detected when calling the dequeue method for
    #     for the first time. The dequeue method will call build method
    #     with the output shapes.
    # Either these two situations will lead to an update to the existing
    # output shapes.
    self._update_output_shapes(per_replica_output_shapes)

# Check if the output shapes are fully defined. This is required in order
# to set them in the feature descriptor field of the tpu embedding config
# proto.
self._check_output_shapes_fully_defined()
