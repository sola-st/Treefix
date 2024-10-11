# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Feature configuration.

    Args:
      table: An instance of `tf.tpu.experimental.embedding.TableConfig`,
        describing the table in which this feature should be looked up.
      max_sequence_length: If positive, the feature is a sequence feature with
        the corresponding maximum sequence length. If the sequence is longer
        than this, it will be truncated. If 0, the feature is not a sequence
        feature.
      validate_weights_and_indices: If true, uses safe_embedding_lookup during
        serving which ensures there are no empty rows and all weights and ids
        are positive at the expense of extra compute cost.
      output_shape: Optional argument to config the output shape of the feature
        activation. If provided, the feature feeding to the `embedding.enqueue`
        has to match the shape (for ragged tensor, the input shape and output
        shape can mismatch). If not provided, the shape can be either provided
        to the `embedding.build` or auto detected at the runtime.
      name: An optional name for the feature, useful for debugging.

    Returns:
      `FeatureConfig`.

    Raises:
      ValueError: if `table` is not an instance of
        `tf.tpu.experimental.embedding.TableConfig`.
      ValueError: if `max_sequence_length` not an integer or is negative.
    """
if not isinstance(table, TableConfig):
    raise ValueError(f"Argument `table` has invalid type {type(table)}. "
                     "Expected `tf.tpu.experimental.embedding.TableConfig`.")

if not isinstance(max_sequence_length, int) or max_sequence_length < 0:
    raise ValueError(
        f"Argument `max_sequence_length` must be an int and must be >= 0. "
        f"Received: {max_sequence_length}")

self.table = table
self.max_sequence_length = max_sequence_length
self.name = name
self.output_shape = TensorShape(output_shape)

if not isinstance(
    validate_weights_and_indices, bool):
    raise ValueError(
        f"Argument `validate_weights_and_indices` must be a boolean. "
        f"Received: {validate_weights_and_indices}")

self.validate_weights_and_indices = validate_weights_and_indices
