# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Traces all functions with the same args and kwargs.

    Args:
      *args: Positional args passed to the original function.
      **kwargs: Keyword args passed to the original function.
    """
args = list(args)
kwargs = kwargs.copy()

for fn in self._functions.values():
    # TODO(kathywu): Replace arguments with broader shapes defined in the
    # input signature.
    if self._expects_training_arg:
        def trace_with_training(value, fn=fn):
            utils.set_training_arg(value, self._training_arg_index, args, kwargs)
            add_trace_to_queue(fn, args, kwargs, value)

        trace_with_training(True)
        trace_with_training(False)
    else:
        add_trace_to_queue(fn, args, kwargs)
