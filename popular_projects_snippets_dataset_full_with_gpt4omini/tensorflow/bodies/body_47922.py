# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
# Turn any slice dicts in the args back into `slice` objects.
# This conversion cannot use nest.flatten/map_structure,
# because dicts are flattened by nest while slices aren't.
# So, map_structure would only see the individual elements in the
# dict.
# This can't use map_structure_up_to either because the 'shallowness' of
# the shallow tree would have to vary depending on if only one dim or
# multiple are being sliced.
new_args = []
for arg in args:
    arg = _dict_to_slice(arg)
    if isinstance(arg, (list, tuple)):
        new_arg = []
        for sub_arg in arg:
            new_arg.append(_dict_to_slice(sub_arg))
        arg = new_arg
    new_args.append(arg)

# Handle the kwargs too.
new_kwargs = {}
for key, value in kwargs.items():
    value = _dict_to_slice(value)
    if isinstance(value, (list, tuple)):
        new_value = []
        for v in value:
            new_value.append(_dict_to_slice(v))
        value = new_value
    new_kwargs[key] = value

exit(original_call(*new_args, **new_kwargs))
