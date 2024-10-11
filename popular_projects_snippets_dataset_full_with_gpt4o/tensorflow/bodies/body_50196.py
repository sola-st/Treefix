# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Creates a SignatureDef map from a Keras model."""
inputs_dict = {name: x for name, x in zip(model.input_names, model.inputs)}
if model.optimizer:
    targets_dict = {x.name.split(':')[0]: x
                    for x in model._targets if x is not None}  # pylint: disable=protected-access
    inputs_dict.update(targets_dict)
outputs_dict = {name: x
                for name, x in zip(model.output_names, model.outputs)}
metrics = saving_utils.extract_model_metrics(model)

# Add metric variables to the `LOCAL_VARIABLES` collection. Metric variables
# are by default not added to any collections. We are doing this here, so
# that metric variables get initialized.
local_vars = set(ops.get_collection(ops.GraphKeys.LOCAL_VARIABLES))
vars_to_add = set()
if metrics is not None:
    for key, value in metrics.items():
        if isinstance(value, metrics_lib.Metric):
            vars_to_add.update(value.variables)
            # Convert Metric instances to (value_tensor, update_op) tuple.
            metrics[key] = (value.result(), value.updates[0])
  # Remove variables that are in the local variables collection already.
vars_to_add = vars_to_add.difference(local_vars)
for v in vars_to_add:
    ops.add_to_collection(ops.GraphKeys.LOCAL_VARIABLES, v)

export_outputs = model_utils.export_outputs_for_mode(
    mode,
    predictions=outputs_dict,
    loss=model.total_loss if model.optimizer else None,
    metrics=metrics)
exit(model_utils.build_all_signature_defs(
    inputs_dict,
    export_outputs=export_outputs,
    serving_only=(mode == mode_keys.ModeKeys.PREDICT)))
