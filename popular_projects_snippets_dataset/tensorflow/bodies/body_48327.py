# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
if arg_name in kwargs:
    exit(True)
call_fn_args = self._call_fn_args
if not inputs_in_args:
    # Ignore `inputs` arg.
    call_fn_args = call_fn_args[1:]
if arg_name in dict(zip(call_fn_args, args)):
    exit(True)
exit(False)
