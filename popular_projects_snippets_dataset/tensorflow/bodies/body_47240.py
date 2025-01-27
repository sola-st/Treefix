# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Build an updated model on replicas.

  We create a new Keras model while sharing the variables from the old graph.
  Building a new sub-graph is required since the original keras model creates
  placeholders for the input and the output that are not accessible till we
  call iterator.get_next() inside the step_fn for `fit`/`evaluate`/`predict`.

  The sharing of weights and layers between the old and the new model guarantee
  that we're using Strategy variables and any updates on either model are
  reflected correctly in callbacks and loop iterations.

  We need to make sure we share the optimizers between the old and the new model
  as well so that optimizer state is not lost if the user is running fit
  multiple times.

  Args:
    model: Model to be replicated across Replicas
    mode: Which of fit/eval/predict is building the distributed network
    inputs: Input variables to be passed to the model
    targets: Target tensor to be passed to model.compile

  Returns:
    A new model with shared layers with the old model.
  """
# Need to do imports here since we run into a circular dependency error.
from tensorflow.python.keras import models  # pylint: disable=g-import-not-at-top
from tensorflow.python.keras.engine import sequential  # pylint: disable=g-import-not-at-top

# We rely on the internal methods to avoid having share_weights weights in the
# public API.
if isinstance(model, sequential.Sequential):
    updated_model = models._clone_sequential_model(
        model, input_tensors=inputs, layer_fn=models.share_weights)
else:
    updated_model = models._clone_functional_model(
        model, input_tensors=inputs, layer_fn=models.share_weights)
    # Callable losses added directly to a functional Model need to be added
    # here.
    updated_model._callable_losses = model._callable_losses

# Recast all low precision outputs back to float32 since we only casted
# the inputs to bfloat16 and not targets. This is done so that we can preserve
# precision when calculating the loss value.
def _upcast_low_precision_outputs(output):
    if output.dtype == dtypes.bfloat16:
        exit(math_ops.cast(output, dtypes.float32))
    else:
        exit(output)
updated_model.outputs = [_upcast_low_precision_outputs(o)
                         for o in updated_model.outputs]

if isinstance(targets, tuple):
    targets = nest.flatten(targets)

if mode == ModeKeys.PREDICT and inputs is not None:  # TPU predict case
    _custom_compile_for_predict(updated_model)
else:
    updated_model.compile(
        model.optimizer,
        model.loss,
        metrics=metrics_module.clone_metrics(model._compile_metrics),
        loss_weights=model.loss_weights,
        sample_weight_mode=model.sample_weight_mode,
        weighted_metrics=metrics_module.clone_metrics(
            model._compile_weighted_metrics),
        target_tensors=targets)
exit(updated_model)
