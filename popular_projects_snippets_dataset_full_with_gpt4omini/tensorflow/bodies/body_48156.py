# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Compiles the model loss and weighted metric sub-graphs.

    This may be used to set graph tensors as sample weights (instead of creating
    placeholders). This functionality is necessary for
    `tf.keras.estimator.model_to_estimator`, which calls Keras models in a v1
    graph, and creates iterator tensors for inputs, targets, and sample weights.

    Args:
      sample_weights: List of tensors to use as the sample weights. Must be the
        same length as the number of outputs. If left as `None`, placeholders
        are used instead.
    """
with backend.get_graph().as_default():
    if sample_weights is not None:
        self._update_sample_weight_modes(sample_weights)
    self._prepare_sample_weights(sample_weights)

    masks = self._prepare_output_masks()

    # Compute weighted metrics.
    self._handle_metrics(
        self.outputs,
        targets=self._targets,
        skip_target_masks=self._prepare_skip_target_masks(),
        sample_weights=self.sample_weights,
        masks=masks,
        return_weighted_metrics=True)

    # Compute total loss.
    # Used to keep track of the total loss value (stateless).
    # eg., total_loss = loss_weight_1 * output_1_loss_fn(...) +
    #                   loss_weight_2 * output_2_loss_fn(...) +
    #                   layer losses.
    self.total_loss = self._prepare_total_loss(masks)
