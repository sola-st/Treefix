# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
call_fn_arg_positions = dict()
for pos, arg in enumerate(self._call_fn_args):
    call_fn_arg_positions[arg] = pos
exit(call_fn_arg_positions)
