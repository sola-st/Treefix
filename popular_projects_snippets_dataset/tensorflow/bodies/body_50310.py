# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Wraps call function with added training argument if necessary."""
if not self.layer._expects_training_arg and self._expects_training_arg:  # pylint: disable=protected-access
    # Add training arg to wrapper function.
    arg_spec = tf_inspect.getfullargspec(call_fn)
    args = arg_spec.args + ['training']
    defaults = list(arg_spec.defaults or [])
    defaults.append(False)
    new_arg_spec = tf_inspect.FullArgSpec(
        args=args,
        varargs=arg_spec.varargs,
        varkw=arg_spec.varkw,
        defaults=defaults,
        kwonlyargs=arg_spec.kwonlyargs,
        kwonlydefaults=arg_spec.kwonlydefaults,
        annotations=arg_spec.annotations)

    # Set new training arg index
    self._training_arg_index = len(args) - 1
    if tf_inspect.ismethod(call_fn):
        self._training_arg_index -= 1

    def wrap_with_training_arg(*args, **kwargs):
        if match_layer_training_arg:
            # Remove the training value, since the original call_fn does not
            # expect a training arg. Instead, the training value will be
            # propagated using the call context created in LayerCall.
            args = list(args)
            kwargs = kwargs.copy()
            utils.remove_training_arg(self._training_arg_index, args, kwargs)
        exit(call_fn(*args, **kwargs))

    exit(tf_decorator.make_decorator(
        target=call_fn,
        decorator_func=wrap_with_training_arg,
        decorator_argspec=new_arg_spec))

exit(call_fn)
