import numpy as np # pragma: no cover

class MockModel: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._expects_training_arg = True # pragma: no cover
        self.loss_functions = [keras.losses.MeanSquaredError()] # pragma: no cover
        self.losses = [] # pragma: no cover
        self.output_names = ['output'] # pragma: no cover
        self.outputs = [np.array([[1.0], [2.0]])] # pragma: no cover
        self._loss_weights_list = [1.0] # pragma: no cover
    def __call__(self, inputs, **kwargs): # pragma: no cover
        return [inputs] # pragma: no cover
training = True # pragma: no cover
inputs = [np.array([[1.0], [2.0]])] # pragma: no cover
class MockNest: # pragma: no cover
    @staticmethod # pragma: no cover
    def flatten(inputs): # pragma: no cover
        return inputs # pragma: no cover
    @staticmethod # pragma: no cover
    def map_structure(func, inputs): # pragma: no cover
        return func(inputs) # pragma: no cover
nest = MockNest() # pragma: no cover
class MockOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def convert_to_tensor_v2_with_dispatch(val): # pragma: no cover
        return val # pragma: no cover
ops = MockOps() # pragma: no cover
targets = [np.array([[1.0], [2.0]])] # pragma: no cover
class MockTrainingUtils: # pragma: no cover
    @staticmethod # pragma: no cover
    def cast_if_floating_dtype_and_mismatch(targets, outs): # pragma: no cover
        return targets # pragma: no cover
    @staticmethod # pragma: no cover
    def cast_if_floating_dtype(val): # pragma: no cover
        return val # pragma: no cover
training_utils_v1 = MockTrainingUtils() # pragma: no cover
sample_weights = [np.array([1, 1])] # pragma: no cover
class MockBackend: # pragma: no cover
    @staticmethod # pragma: no cover
    def name_scope(name): # pragma: no cover
        return name # pragma: no cover
backend = MockBackend() # pragma: no cover
class MockMathOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def cast(val, dtype): # pragma: no cover
        return val # pragma: no cover
    @staticmethod # pragma: no cover
    def add_n(tensors): # pragma: no cover
        return sum(tensors) # pragma: no cover
math_ops = MockMathOps() # pragma: no cover
class MockLossesUtils: # pragma: no cover
    class ReductionV2: # pragma: no cover
        AUTO = 'auto' # pragma: no cover
        SUM_OVER_BATCH_SIZE = 'sum_over_batch_size' # pragma: no cover
    @staticmethod # pragma: no cover
    def squeeze_or_expand_dimensions(mask, sample_weight=None): # pragma: no cover
        return mask, None, sample_weight # pragma: no cover
    @staticmethod # pragma: no cover
    def compute_weighted_loss(per_sample_losses, sample_weight=None, reduction=None): # pragma: no cover
        return per_sample_losses # pragma: no cover
    @staticmethod # pragma: no cover
    def reduce_weighted_loss(weighted_losses, reduction=None): # pragma: no cover
        return np.mean(weighted_losses) # pragma: no cover
    @staticmethod # pragma: no cover
    def scale_loss_for_distribution(loss): # pragma: no cover
        return loss # pragma: no cover
losses_utils = MockLossesUtils() # pragma: no cover

import numpy as np # pragma: no cover

class MockModel: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._expects_training_arg = True # pragma: no cover
        self.losses = [] # pragma: no cover
        self.output_names = ['output'] # pragma: no cover
        self.outputs = [np.array([[1.0], [2.0]])] # pragma: no cover
        self._loss_weights_list = [1.0] # pragma: no cover
    def __call__(self, inputs, **kwargs): # pragma: no cover
        return self.outputs # pragma: no cover
model = MockModel() # pragma: no cover
training = True # pragma: no cover
inputs = [np.array([[1.0, 2.0]])] # pragma: no cover
class MockNest: # pragma: no cover
    @staticmethod # pragma: no cover
    def flatten(x): # pragma: no cover
        return x # pragma: no cover
    @staticmethod # pragma: no cover
    def map_structure(fn, x): # pragma: no cover
        return fn(x) # pragma: no cover
nest = MockNest() # pragma: no cover
class MockOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def convert_to_tensor_v2_with_dispatch(x): # pragma: no cover
        return x # pragma: no cover
ops = MockOps() # pragma: no cover
targets = [np.array([[1.0], [2.0]])] # pragma: no cover
class MockTrainingUtils: # pragma: no cover
    @staticmethod # pragma: no cover
    def cast_if_floating_dtype_and_mismatch(targets, outs): # pragma: no cover
        return targets # pragma: no cover
    @staticmethod # pragma: no cover
    def cast_if_floating_dtype(val): # pragma: no cover
        return val # pragma: no cover
training_utils_v1 = MockTrainingUtils() # pragma: no cover
sample_weights = [np.array([1.0, 1.0])] # pragma: no cover
class MockBackend: # pragma: no cover
    @staticmethod # pragma: no cover
    def name_scope(name): # pragma: no cover
        return name # pragma: no cover
backend = MockBackend() # pragma: no cover
class MockMathOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def cast(x, dtype): # pragma: no cover
        return x # pragma: no cover
    @staticmethod # pragma: no cover
    def add_n(tensors): # pragma: no cover
        return sum(tensors) # pragma: no cover
math_ops = MockMathOps() # pragma: no cover
class MockLossesUtils: # pragma: no cover
    class ReductionV2: # pragma: no cover
        AUTO = 'auto' # pragma: no cover
        SUM_OVER_BATCH_SIZE = 'sum_over_batch_size' # pragma: no cover
    @staticmethod # pragma: no cover
    def squeeze_or_expand_dimensions(mask, sample_weight=None): # pragma: no cover
        return mask, None, sample_weight # pragma: no cover
    @staticmethod # pragma: no cover
    def compute_weighted_loss(losses, sample_weight=None, reduction=None): # pragma: no cover
        return losses # pragma: no cover
    @staticmethod # pragma: no cover
    def reduce_weighted_loss(weighted_losses, reduction=None): # pragma: no cover
        return np.sum(weighted_losses) # pragma: no cover
    @staticmethod # pragma: no cover
    def scale_loss_for_distribution(loss): # pragma: no cover
        return loss # pragma: no cover
losses_utils = MockLossesUtils() # pragma: no cover

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
_l_(6675)
kwargs = {}
_l_(6676)
if model._expects_training_arg:
    _l_(6678)

    kwargs['training'] = training
    _l_(6677)
if len(inputs) == 1 and not isinstance(inputs, dict):
    _l_(6680)

    inputs = inputs[0]
    _l_(6679)

# Allow mixed `NumPy` and `EagerTensor` input here.
if any(
    isinstance(input_t, (np.ndarray, float, int))
    for input_t in nest.flatten(inputs)):
    _l_(6682)

    inputs = nest.map_structure(ops.convert_to_tensor_v2_with_dispatch, inputs)
    _l_(6681)

outs = model(inputs, **kwargs)
_l_(6683)
outs = nest.flatten(outs)
_l_(6684)

if targets:
    _l_(6686)

    targets = training_utils_v1.cast_if_floating_dtype_and_mismatch(
        targets, outs)
    _l_(6685)
# TODO(sallymatson/psv): check if we should do same mismatch fix for weights
if sample_weights:
    _l_(6688)

    sample_weights = [
        training_utils_v1.cast_if_floating_dtype(
            ops.convert_to_tensor_v2_with_dispatch(val))
        if val is not None else None for val in sample_weights
    ]
    _l_(6687)

masks = [getattr(t, '_keras_mask', None) for t in outs]
_l_(6689)
targets = nest.flatten(targets)
_l_(6690)

# Used to keep track of individual output losses.
output_losses = []
_l_(6691)

with backend.name_scope('loss'):
    _l_(6725)

    loss_fns = [
        loss_fn for loss_fn in model.loss_functions if loss_fn is not None
    ]
    _l_(6692)
    custom_losses = model.losses  # Regularization losses
    _l_(6693)  # Regularization losses

    if not loss_fns and not custom_losses:
        _l_(6697)

        if training:
            _l_(6696)

            raise ValueError('The model cannot be trained '
                             'because it has no loss to optimize.')
            _l_(6694)
        else:
            raise ValueError('The model cannot be evaluated '
                             'because it has no loss to compute.')
            _l_(6695)

    for i, loss_fn in enumerate(loss_fns):
        _l_(6722)

        weights = sample_weights[i] if sample_weights else None
        _l_(6698)
        mask = masks[i]
        _l_(6699)
        with backend.name_scope(model.output_names[i] + '_loss'):
            _l_(6716)

            if mask is not None:
                _l_(6706)

                mask = math_ops.cast(mask, outs[i].dtype)
                _l_(6700)
                # Update weights with mask.
                if weights is None:
                    _l_(6705)

                    weights = mask
                    _l_(6701)
                else:
                    # Update dimensions of weights to match with mask if possible.
                    weights = math_ops.cast(weights, outs[i].dtype)
                    _l_(6702)
                    mask, _, weights = (
                        losses_utils.squeeze_or_expand_dimensions(
                            mask, sample_weight=weights))
                    _l_(6703)
                    weights *= mask
                    _l_(6704)

            if hasattr(loss_fn, 'reduction'):
                _l_(6715)

                per_sample_losses = loss_fn.call(targets[i], outs[i])
                _l_(6707)
                weighted_losses = losses_utils.compute_weighted_loss(
                    per_sample_losses,
                    sample_weight=weights,
                    reduction=losses_utils.ReductionV2.NONE)
                _l_(6708)
                loss_reduction = loss_fn.reduction
                _l_(6709)

                # `AUTO` loss reduction defaults to `SUM_OVER_BATCH_SIZE` for all
                # compile use cases.
                if loss_reduction == losses_utils.ReductionV2.AUTO:
                    _l_(6711)

                    loss_reduction = losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE
                    _l_(6710)

                # Compute the stateless loss value.
                output_loss = losses_utils.reduce_weighted_loss(
                    weighted_losses, reduction=loss_reduction)
                _l_(6712)
            else:
                # Compute the stateless loss value for a custom loss class.
                # Here we assume that the class takes care of loss reduction
                # because if this class returns a vector value we cannot
                # differentiate between use case where a custom optimizer
                # expects a vector loss value vs unreduced per-sample loss value.
                output_loss = loss_fn(targets[i], outs[i], sample_weight=weights)
                _l_(6713)
                loss_reduction = losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE
                _l_(6714)

      # If the number of outputs is 1 then we don't append the loss metric
      # associated with each model output. When there are multiple outputs
      # associated with a model, each output's loss is calculated and returned
      # as part of the loss_metrics.
        if len(model.outputs) > 1:
            _l_(6718)

            # Keep track of the stateful output loss result.
            output_losses.append(output_loss_metrics[i](output_loss))
            _l_(6717)

        # Scale output loss for distribution. For custom losses we assume
        # reduction was mean.
        if loss_reduction == losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE:
            _l_(6720)

            output_loss = losses_utils.scale_loss_for_distribution(output_loss)
            _l_(6719)
        total_loss += model._loss_weights_list[i] * output_loss
        _l_(6721)

    # Add regularization losses
    if custom_losses:
        _l_(6724)

        total_loss += losses_utils.scale_loss_for_distribution(
            math_ops.add_n(custom_losses))
        _l_(6723)
aux = (outs, total_loss, output_losses, masks)
_l_(6726)
exit(aux)
