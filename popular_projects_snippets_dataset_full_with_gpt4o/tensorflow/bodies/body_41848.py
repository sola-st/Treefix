# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_utils.py
"""Restore captures for the concrete function.

  Used at deserialization time.  For functions that are being deserialized,
  saved model restores objects that tensors were captured from, but functions
  only know about their tensors -- object information is destroyed by tracing.
  This additional logic extracts the tensors which the function originally
  captured.

  Args:
    concrete_function: the concrete function for which to restore captures
    inputs: a list tensors or other Python objects (such as variables) which
      contain tensors that were originally captured by the function
  """
bound_inputs = [get_tensor_from_node(obj) for obj in inputs]
bound_variables = [
    obj for obj in inputs
    if isinstance(obj, (variables_lib.Variable,
                        resource_variable_ops.BaseResourceVariable))
]
# TODO(b/205010575): This is only injecting the captured inputs into the
# concrete function, note that we did not modify the FuncGraph
# itself.
captured_inputs_list = []
concrete_function.set_variables(bound_variables)
if bound_inputs:
    for bound_input, internal_capture in zip(
        bound_inputs, concrete_function.inputs[-len(bound_inputs):]):
        # Distributed inputs have special logic for capturing, so we call their
        # custom restoration methods
        if hasattr(bound_input, "__tf_experimental_restore_capture__"):
            captured_inputs_list.append(
                bound_input.__tf_experimental_restore_capture__(
                    concrete_function, internal_capture))
        else:
            captured_inputs_list.append(bound_input)
            concrete_function.graph.replace_capture(bound_input, internal_capture)
            if internal_capture.dtype == dtypes.resource:
                if resource_variable_ops.is_resource_variable(bound_input):
                    try:
                        handle = bound_input.handle
                    except ValueError:
                        # For mirrored variables we'll copy handle data for components
                        # as they get captured.
                        pass
                    else:
                        handle_data_util.copy_handle_data(handle, internal_capture)
                else:
                    # TODO(b/213451747): Remove need to call copy_handle_data
                    handle_data_util.copy_handle_data(bound_input, internal_capture)
        # Setting "captures" first means "capture" won't create a new
        # placeholder for this input.
            concrete_function.graph.capture(bound_input)

if any([inp is None for inp in captured_inputs_list]):
    warnings.warn("Trying to load ShardedVariables using tf.saved_model.load. "
                  "This won't work if using a tf.distribute.Strategy, and may "
                  "use excess memory if not using a Strategy. Ignore this "
                  "warning if using tf.keras.models.load_model.")
concrete_function.set_external_captures(captured_inputs_list)
