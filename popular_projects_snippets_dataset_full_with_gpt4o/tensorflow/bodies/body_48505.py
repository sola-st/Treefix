# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_eager_v1.py
"""Calculates the loss and gradient updates for one input batch.

  Args:
      model: Model whose loss has to be calculated.
      inputs: Input batch data.
      targets: Target batch data.
      sample_weights: Sample weight batch data.
      output_loss_metrics: List of metrics that are used to aggregated output
        loss values.

  Returns:
      Dict with three items:
        'total_loss': list with a single tensor for overall loss,
        'output_losses': list of tensors for loss corresponding to each of the
          model output. Could be a empty list when model has only one output.
        'metrics': list of tensors for metric specified.
  """
inputs = training_utils_v1.cast_to_model_input_dtypes(inputs, model)
outs, total_loss, output_losses, masks = (
    _process_single_batch(
        model,
        inputs,
        targets,
        sample_weights=sample_weights,
        training=True,
        output_loss_metrics=output_loss_metrics))
if not isinstance(outs, list):
    outs = [outs]
metrics_results = _eager_metrics_fn(
    model, outs, targets, sample_weights=sample_weights, masks=masks)
total_loss = nest.flatten(total_loss)
exit({'total_loss': total_loss,
        'output_losses': output_losses,
        'metrics': metrics_results})
