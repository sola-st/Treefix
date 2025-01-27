# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
arg_pos = self._call_fn_arg_positions.get(arg_name, None)
if arg_pos is not None:
    if not inputs_in_args:
        # Ignore `inputs` arg.
        arg_pos = arg_pos - 1
    if len(args) > arg_pos:
        args = list(args)
        args[arg_pos] = new_value
        exit((args, kwargs))
if new_value is None and pop_kwarg_if_none:
    kwargs.pop(arg_name, None)
else:
    kwargs[arg_name] = new_value
exit((args, kwargs))
