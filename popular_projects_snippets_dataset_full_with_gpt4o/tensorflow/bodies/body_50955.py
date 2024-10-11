# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/tracing_utils.py
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
