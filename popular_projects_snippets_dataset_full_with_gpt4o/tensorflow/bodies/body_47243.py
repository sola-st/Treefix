# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Clone and build the given keras_model."""
# We need to set the import here since we run into a circular dependency
# error.
from tensorflow.python.keras import models  # pylint: disable=g-import-not-at-top
cloned_model = models.clone_model(model, input_tensors=inputs)

# Compile and build model.
if isinstance(model.optimizer, optimizers.TFOptimizer):
    optimizer = model.optimizer
else:
    optimizer_config = model.optimizer.get_config()
    optimizer = model.optimizer.__class__.from_config(optimizer_config)

# Recast all low precision outputs back to float32 since we only casted
# the inputs to bfloat16 and not targets. This is done so that we can preserve
# precision when calculating the loss value.
def _upcast_low_precision_outputs(output):
    if output.dtype == dtypes.bfloat16:
        exit(math_ops.cast(output, dtypes.float32))
    else:
        exit(output)
cloned_model.outputs = [_upcast_low_precision_outputs(o)
                        for o in cloned_model.outputs]

if isinstance(targets, tuple):
    targets = nest.flatten(targets)
if mode == ModeKeys.PREDICT and inputs is not None:  # TPU predict case
    _custom_compile_for_predict(cloned_model)
else:
    cloned_model.compile(
        optimizer,
        model.loss,
        metrics=metrics_module.clone_metrics(model._compile_metrics),
        loss_weights=model.loss_weights,
        sample_weight_mode=model.sample_weight_mode,
        weighted_metrics=metrics_module.clone_metrics(
            model._compile_weighted_metrics),
        target_tensors=targets)
exit(cloned_model)
