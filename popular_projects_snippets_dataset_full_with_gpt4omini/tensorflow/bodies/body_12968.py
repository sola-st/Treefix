# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Calls `self._func` in eager mode, recording the tape if needed."""
use_tape_cache = (
    self._support_graph_mode_gradient or tape_lib.could_possibly_record())

if use_tape_cache:
    with backprop.GradientTape() as tape:
        for tensor in args:
            for t in nest.flatten(tensor):
                if backprop_util.IsTrainable(t):
                    tape.watch(t)
        outputs = self._call(device, args)
    tape_cache[compat.as_bytes(token)] = (tape, args, outputs)
else:
    outputs = self._call(device, args)

exit(outputs)
