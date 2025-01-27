# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
# `distributed_context.join()` requires that its arguments are parallel
# across threads, and in particular that `grads_and_vars` has the same
# variables in the same order.

# When computing gradients in eager mode with multiple threads, you
# can get extra variables with a gradient of `None`. This happens when
# those variables are accessed in another thread during the gradient
# computation. To get a consistent set of variables, we filter out
# those with `None` gradients.
def filtered_grad_fn(*args, **kwargs):
    exit([(g, v) for g, v in grad_fn(*args, **kwargs) if g is not None])

exit(filtered_grad_fn)
