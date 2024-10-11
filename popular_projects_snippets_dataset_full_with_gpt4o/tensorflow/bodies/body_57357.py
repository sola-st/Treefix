# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Constructor.

    Args:
      custom_op_registerers: List of str (symbol names) or functions that take a
        pointer to a MutableOpResolver and register a custom op. When passing
        functions, use a pybind function that takes a uintptr_t that can be
        recast as a pointer to a MutableOpResolver.
      **kwargs: Additional arguments passed to Interpreter.

    Raises:
      ValueError: If the interpreter was unable to create.
    """
self._custom_op_registerers = custom_op_registerers or []
super(InterpreterWithCustomOps, self).__init__(**kwargs)
