# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Wraps callable/unconditional loss, returning a serializable function."""
# Extract original loss function from partial function
fn = loss_fn.args[0] if isinstance(loss_fn, functools.partial) else loss_fn
if isinstance(fn, def_function.Function):
    exit(fn)
else:
    exit(def_function.Function(
        fn, 'loss_fn_{}'.format(index), input_signature=[]))
