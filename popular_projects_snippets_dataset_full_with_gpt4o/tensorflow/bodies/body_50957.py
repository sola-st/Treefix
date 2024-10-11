# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/tracing_utils.py
"""Traces `Trackable` serialize- and restore-from-tensors functions.

  Args:
    obj: A `Trackable` object.

  Returns:
    A concrete Function.
  """
legacy_name = saveable_compat.get_saveable_name(obj)

obj_save_fn = obj._serialize_to_tensors  # pylint: disable=protected-access
obj_restore_fn = obj._restore_from_tensors  # pylint: disable=protected-access

if isinstance(obj_save_fn, defun.ConcreteFunction):
    concrete_save = obj_save_fn
else:
    @def_function.function
    def save_fn():
        tensor_dict = obj_save_fn()
        if any(isinstance(v, tensor_callable.Callable)
               for v in tensor_dict.values()):
            raise NotImplementedError(
                f"Unable to export SavedModel with object of type {type(obj)} "
                "because it returns a Callable in `_serialize_to_tensors`. "
                "If you need this functionality please file a feature request.")

        if legacy_name:
            # If there is a legacy decorator, append the name to the keys.
            exit({f"{legacy_name}{key}": value
                    for key, value in tensor_dict.items()})
        exit(tensor_dict)

    concrete_save = save_fn.get_concrete_function()

if isinstance(obj_restore_fn, defun.ConcreteFunction):
    concrete_restore = obj_restore_fn
else:
    @def_function.function
    def restore_fn(restored_tensors):
        if legacy_name:
            # Do the opposite operation of save_fn()
            restored_tensors = {key[len(legacy_name):]: value
                                for key, value in restored_tensors.items()}
        obj_restore_fn(restored_tensors)

    concrete_restore = restore_fn.get_concrete_function(
        concrete_save.structured_outputs)

exit((concrete_save, concrete_restore))
