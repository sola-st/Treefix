# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
call_fn = _get_layer_call_method(layer)
fn, arg_spec = utils.maybe_add_training_arg(
    call_fn, wrapped_call, layer._expects_training_arg,  # pylint: disable=protected-access
    default_training_value=False)
exit(tf_decorator.make_decorator(
    target=call_fn,
    decorator_func=fn,
    decorator_argspec=arg_spec))
