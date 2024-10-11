# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Handle TPUEmbedding.

    Args:
      tpu_embedding: TPUEmbedding object to be handled.

    Raises:
      AttributeError: if the input trackable is not TPUEmbedding type.
    """
if not isinstance(tpu_embedding, TPUEmbedding):
    raise AttributeError("Expecting TPUEmbedding type; got %s" %
                         type(tpu_embedding))

# Create a dummy TPUEmbedding object and add it to the object_map. This is
# to prevent the TPUEmbedding's save_callback from being triggered because
# the embedding values have already being retrieved by AsyncCheckpoint.
# pylint: disable=protected-access
new_embedding = TPUEmbedding(
    feature_config=tpu_embedding._feature_config,
    optimizer=tpu_embedding._table_config[0].optimizer,
    pipeline_execution_with_tensor_core=tpu_embedding
    ._pipeline_execution_with_tensor_core)
self._object_map[tpu_embedding] = new_embedding
# pylint: enable=protected-access

if tpu_embedding not in self._tpu_embedding_objects:
    self._tpu_embedding_objects.append(tpu_embedding)
