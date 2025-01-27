# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/tape.py
self._c_tape = _tape.Tape(persistent)
ctx = context_stack.get_default()
self._tape_context = _tape.TapeContext(
    ctx, self._c_tape, gradient_registry.get_global_registry())
self._ctx_manager = None
