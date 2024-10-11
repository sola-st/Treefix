# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Initialize the _TrainingEndpoint.

    Note that the output and output_name should be stable as long as the model
    structure doesn't change. The training_target suppose to be mutable since
    the information is provided via `compile()`

    Args:
      output: the output tensor of the model.
      output_name: the unique name of the output tensor.
      loss_fn: the loss function for the output tensor.
      loss_weight: float, the weights for the loss.
      training_target: the _TrainingTarget for the model.
      output_loss_metric: the metric object for the loss function.
      sample_weight: the weights for how a sample is weighted during metric and
        loss calculation. Could be None.
      sample_weight_mode: string, 'temporal', 'samplewise' or None. The mode for
        how the sample_weight is populated.
    """
self._output = output
self._output_name = output_name
self._loss_fn = loss_fn
self._loss_weight = loss_weight
self._training_target = training_target
self._output_loss_metric = output_loss_metric
self._sample_weight = sample_weight
self._sample_weight_mode = sample_weight_mode
