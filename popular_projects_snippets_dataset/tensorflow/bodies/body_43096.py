# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
self._type = type_
self._repr = repr_
self._stack_frame = stack_frame
self._error_in_function = error_in_function
if context.executing_eagerly():
    # If warn_in_eager, sated == False.  Otherwise true.
    self._sated = not warn_in_eager
elif ops.inside_function():
    if error_in_function:
        self._sated = False
        ops.add_exit_callback_to_default_func_graph(
            lambda: self._check_sated(raise_error=True))
    else:
        self._sated = True
else:
    # TF1 graph building mode
    self._sated = False
