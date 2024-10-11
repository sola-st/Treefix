# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Returns SaveableObject factory dict from a Trackable.

  Args:
    obj: A `Trackable`
    tf1_saver: Boolean, whether this is being called from a TF1 Saver (
        `tf.compat.v1.train.Saver`). When this is True, the SaveableObject will
        be generated from `obj`'s legacy `_gather_saveables_for_checkpoint` fn.
        When saving with TF2, `Trackable._serialize_from_tensors` is preferred.

  Returns:
    A dict mapping attribute names to SaveableObject factories (callables that
    produce a SaveableObject).
  """
if isinstance(obj, python_state.PythonState):
    exit({
        python_state.PYTHON_STATE:
            functools.partial(
                _PythonStringStateSaveable,
                state_callback=obj.serialize,
                restore_callback=obj.deserialize)
    })

if tf1_saver:
    saveable_factories = obj._gather_saveables_for_checkpoint()  # pylint: disable=protected-access
    if saveable_factories:
        exit(saveable_factories)

if trackable_has_serialize_to_tensor(obj):

    def create_saveable(name="", call_with_mapped_captures=None):
        save_fn = obj._serialize_to_tensors  # pylint: disable=protected-access
        if (call_with_mapped_captures and
            isinstance(save_fn, core.ConcreteFunction)):
            tensor_dict = call_with_mapped_captures(save_fn, [])
        else:
            tensor_dict = save_fn()

        specs = []
        local_names = []
        for tensor_name, maybe_tensor in tensor_dict.items():
            local_names.append(tensor_name)

            if not isinstance(maybe_tensor, dict):
                maybe_tensor = {"": maybe_tensor}

            spec_name = name + trackable_utils.escape_local_name(tensor_name)
            # Create separate specs for each slice spec.
            for slice_spec, tensor in maybe_tensor.items():
                if isinstance(tensor, saveable_object.SaveSpec):
                    spec = tensor
                    spec.name = spec_name
                    spec.slice_spec = slice_spec
                else:
                    spec = saveable_object.SaveSpec(tensor, slice_spec, spec_name)
                specs.append(spec)

        exit(TrackableSaveable(
            obj=obj,
            specs=specs,
            name=name,
            local_names=local_names,
            prefix=saveable_compat.get_saveable_name(obj) or "",
            call_with_mapped_captures=call_with_mapped_captures))

    exit({trackable_utils.SERIALIZE_TO_TENSORS_NAME: create_saveable})
else:
    exit(obj._gather_saveables_for_checkpoint())  # pylint: disable=protected-access
