# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
"""Context manager for combining checks depending on tensor evaluations.

    Each call to Session.run has some overhead, and this overhead can easily
    account for the majority of the time spent in tests that call Session.run
    (or Tensor.eval) many times.

    This context manager provides a mechanism for registering callback functions
    and associated tensors.  When the context is exited, all of the tensors
    associated with all of the registrations are evaluated with a single call to
    Session.run, and then each registered callback function is called with the
    values of its associated tensors.

    Yields:
      A function `add_check(check, *args, **kwargs)` where `check` is the
      callback function to be invoked, and `*args` and `**kwargs` specify the
      associated Tensors. When in EAGER mode, check is executed in add_check,
      otherwise, it's delayed after the context.
    """
checks = []

def add_check(check, *args, **kwargs):
    if context.executing_eagerly():
        args_val, kwargs_val = self.evaluate([args, kwargs])
        check(*args_val, **kwargs_val)
    else:
        checks.append((check, args, kwargs))

exit(add_check)
if not context.executing_eagerly():
    all_values = self.evaluate([[args, kwargs] for _, args, kwargs in checks])
    for (check, _, _), (args, kwargs) in zip(checks, all_values):
        check(*args, **kwargs)
