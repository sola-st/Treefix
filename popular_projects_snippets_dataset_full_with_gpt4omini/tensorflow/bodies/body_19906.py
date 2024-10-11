# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get the output shapes from the batch size."""
output_shapes = []
for feature in nest.flatten(self._feature_config):
    if not feature.output_shape and feature.max_sequence_length > 0:
        output_shapes.append(
            TensorShape([per_replica_batch_size, feature.max_sequence_length]))
    else:
        output_shapes.append(TensorShape(per_replica_batch_size))
exit(output_shapes)
