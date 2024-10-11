# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_eager_v1.py
"""Calculate the loss and gradient for one input batch.

     The model weights are updated if training is set to True.

  Args:
      model: Model whose loss has to be calculated.
      inputs: List of input arrays.
      targets: List of target arrays.
      output_loss_metrics: List of metrics that are used to aggregated output
        loss values.
      sample_weights: Optional list of sample weight arrays.
      training: The boolean represents if the weights of the model are updated.
              'fit' methods will set this to True while 'evaluate' methods will
              set this to False.

  Returns:
      output of the model, total loss, the loss and the mask
      associated with each output.

  Raises:
      ValueError: If the model has no loss to optimize.
  """
with backend.eager_learning_phase_scope(1 if training else 0), \
      training_utils.RespectCompiledTrainableState(model):
    with GradientTape() as tape:
        outs, total_loss, output_losses, masks = (
            _model_loss(
                model,
                inputs,
                targets,
                output_loss_metrics=output_loss_metrics,
                sample_weights=sample_weights,
                training=training))
        if isinstance(model.optimizer, loss_scale_optimizer.LossScaleOptimizer):
            scaled_total_loss = model.optimizer.get_scaled_loss(total_loss)
        else:
            scaled_total_loss = total_loss
    if training:
        trainable_weights = model.trainable_weights
        if trainable_weights:
            # TODO(tanzheny) b/132690565: Provide mechanism for user to override
            # model.train_on_batch.
            if hasattr(model, '_backwards'):
                model._backwards(tape, scaled_total_loss)
            else:
                grads = tape.gradient(scaled_total_loss, trainable_weights)
                if isinstance(model.optimizer,
                              loss_scale_optimizer.LossScaleOptimizer):
                    grads = model.optimizer.get_unscaled_gradients(grads)
                model.optimizer.apply_gradients(zip(grads, trainable_weights))
        else:
            logging.warning('The list of trainable weights is empty. Make sure that'
                            ' you are not setting model.trainable to False before '
                            'compiling the model.')
    exit((outs, total_loss, output_losses, masks))
