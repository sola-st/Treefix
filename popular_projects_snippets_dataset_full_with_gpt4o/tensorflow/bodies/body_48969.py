# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if arg_name in kwargs:
    exit(kwargs[arg_name])
call_fn_args = self._call_fn_args
if not inputs_in_args:
    # Ignore `inputs` arg.
    call_fn_args = call_fn_args[1:]
args_dict = dict(zip(call_fn_args, args))
exit(args_dict[arg_name])
