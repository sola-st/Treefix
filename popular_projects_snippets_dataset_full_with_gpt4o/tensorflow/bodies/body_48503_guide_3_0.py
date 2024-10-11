import numpy as np # pragma: no cover

class MockLossFunction: # pragma: no cover
    def call(self, y_true, y_pred): # pragma: no cover
        return tf.abs(y_true - y_pred) # pragma: no cover
 # pragma: no cover
class MockMetric: # pragma: no cover
    def __call__(self, value): # pragma: no cover
        return value # pragma: no cover
 # pragma: no cover
Mock = type('Mock', (object,), {}) # pragma: no cover
 # pragma: no cover
model = Mock() # pragma: no cover
model._expects_training_arg = True # pragma: no cover
model.loss_functions = [MockLossFunction()] # pragma: no cover
model._loss_weights_list = [1.0] # pragma: no cover
model.outputs = [np.array([1])] # pragma: no cover
model.output_names = ['output'] # pragma: no cover
model.__call__ = lambda inputs, training: tf.convert_to_tensor(inputs) # pragma: no cover
inputs = [np.array([1.0])] # pragma: no cover
targets = [np.array([1.5])] # pragma: no cover
output_loss_metrics = [MockMetric()] # pragma: no cover
sample_weights = [np.array([1.0])] # pragma: no cover
training = True # pragma: no cover
 # pragma: no cover
def mock_cast_if_floating_dtype_and_mismatch(targets, outs): # pragma: no cover
    return targets # pragma: no cover
 # pragma: no cover
def mock_cast_if_floating_dtype(val): # pragma: no cover
    return val # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_eager_v1.py
from l3.Runtime import _l_
"""Calculates the loss for a given model.

  Args:
      model: The model on which metrics are being calculated.
      inputs: Either a dictionary of inputs to the model or a list of input
        arrays.
      targets: List of target arrays.
      output_loss_metrics: List of metrics that are used to aggregated output
        loss values.
      sample_weights: Optional list of sample weight arrays.
      training: Whether the model should be run in inference or training mode.

  Returns:
     Returns the model output, total loss, loss value calculated using the
     specified loss function and masks for each output. The total loss includes
     regularization losses and applies masking and sample weighting
     to the loss value.
  """
# TODO(psv): Dedup code here with graph mode prepare_total_loss() fn.
# Used to keep track of the total loss value (stateless).
# eg., total_loss = loss_weight_1 * output_1_loss_fn(...) +
#                   loss_weight_2 * output_2_loss_fn(...) +
#                   layer losses.
total_loss = 0
_l_(18978)
kwargs = {}
_l_(18979)
if model._expects_training_arg:
    _l_(18981)

    kwargs['training'] = training
    _l_(18980)
if len(inputs) == 1 and not isinstance(inputs, dict):
    _l_(18983)

    inputs = inputs[0]
    _l_(18982)

# Allow mixed `NumPy` and `EagerTensor` input here.
if any(
    isinstance(input_t, (np.ndarray, float, int))
    for input_t in nest.flatten(inputs)):
    _l_(18985)

    inputs = nest.map_structure(ops.convert_to_tensor_v2_with_dispatch, inputs)
    _l_(18984)

outs = model(inputs, **kwargs)
_l_(18986)
outs = nest.flatten(outs)
_l_(18987)

if targets:
    _l_(18989)

    targets = training_utils_v1.cast_if_floating_dtype_and_mismatch(
        targets, outs)
    _l_(18988)
# TODO(sallymatson/psv): check if we should do same mismatch fix for weights
if sample_weights:
    _l_(18991)

    sample_weights = [
        training_utils_v1.cast_if_floating_dtype(
            ops.convert_to_tensor_v2_with_dispatch(val))
        if val is not None else None for val in sample_weights
    ]
    _l_(18990)

masks = [getattr(t, '_keras_mask', None) for t in outs]
_l_(18992)
targets = nest.flatten(targets)
_l_(18993)

# Used to keep track of individual output losses.
output_losses = []
_l_(18994)

with backend.name_scope('loss'):
    _l_(19028)

    loss_fns = [
        loss_fn for loss_fn in model.loss_functions if loss_fn is not None
    ]
    _l_(18995)
    custom_losses = model.losses  # Regularization losses
    _l_(18996)  # Regularization losses

    if not loss_fns and not custom_losses:
        _l_(19000)

        if training:
            _l_(18999)

            raise ValueError('The model cannot be trained '
                             'because it has no loss to optimize.')
            _l_(18997)
        else:
            raise ValueError('The model cannot be evaluated '
                             'because it has no loss to compute.')
            _l_(18998)

    for i, loss_fn in enumerate(loss_fns):
        _l_(19025)

        weights = sample_weights[i] if sample_weights else None
        _l_(19001)
        mask = masks[i]
        _l_(19002)
        with backend.name_scope(model.output_names[i] + '_loss'):
            _l_(19019)

            if mask is not None:
                _l_(19009)

                mask = math_ops.cast(mask, outs[i].dtype)
                _l_(19003)
                # Update weights with mask.
                if weights is None:
                    _l_(19008)

                    weights = mask
                    _l_(19004)
                else:
                    # Update dimensions of weights to match with mask if possible.
                    weights = math_ops.cast(weights, outs[i].dtype)
                    _l_(19005)
                    mask, _, weights = (
                        losses_utils.squeeze_or_expand_dimensions(
                            mask, sample_weight=weights))
                    _l_(19006)
                    weights *= mask
                    _l_(19007)

            if hasattr(loss_fn, 'reduction'):
                _l_(19018)

                per_sample_losses = loss_fn.call(targets[i], outs[i])
                _l_(19010)
                weighted_losses = losses_utils.compute_weighted_loss(
                    per_sample_losses,
                    sample_weight=weights,
                    reduction=losses_utils.ReductionV2.NONE)
                _l_(19011)
                loss_reduction = loss_fn.reduction
                _l_(19012)

                # `AUTO` loss reduction defaults to `SUM_OVER_BATCH_SIZE` for all
                # compile use cases.
                if loss_reduction == losses_utils.ReductionV2.AUTO:
                    _l_(19014)

                    loss_reduction = losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE
                    _l_(19013)

                # Compute the stateless loss value.
                output_loss = losses_utils.reduce_weighted_loss(
                    weighted_losses, reduction=loss_reduction)
                _l_(19015)
            else:
                # Compute the stateless loss value for a custom loss class.
                # Here we assume that the class takes care of loss reduction
                # because if this class returns a vector value we cannot
                # differentiate between use case where a custom optimizer
                # expects a vector loss value vs unreduced per-sample loss value.
                output_loss = loss_fn(targets[i], outs[i], sample_weight=weights)
                _l_(19016)
                loss_reduction = losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE
                _l_(19017)

      # If the number of outputs is 1 then we don't append the loss metric
      # associated with each model output. When there are multiple outputs
      # associated with a model, each output's loss is calculated and returned
      # as part of the loss_metrics.
        if len(model.outputs) > 1:
            _l_(19021)

            # Keep track of the stateful output loss result.
            output_losses.append(output_loss_metrics[i](output_loss))
            _l_(19020)

        # Scale output loss for distribution. For custom losses we assume
        # reduction was mean.
        if loss_reduction == losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE:
            _l_(19023)

            output_loss = losses_utils.scale_loss_for_distribution(output_loss)
            _l_(19022)
        total_loss += model._loss_weights_list[i] * output_loss
        _l_(19024)

    # Add regularization losses
    if custom_losses:
        _l_(19027)

        total_loss += losses_utils.scale_loss_for_distribution(
            math_ops.add_n(custom_losses))
        _l_(19026)
aux = (outs, total_loss, output_losses, masks)
_l_(19029)
exit(aux)
