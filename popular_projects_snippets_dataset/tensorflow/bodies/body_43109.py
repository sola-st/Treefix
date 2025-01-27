# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
"""Function wrapper that ensures the function's output is used.

  If the output is not used, a `logging.error` is logged.  If
  `error_in_function` is set, then a `RuntimeError` will be raised at the
  end of function tracing if the output is not used by that point.

  An output is marked as used if any of its attributes are read, modified, or
  updated.  Examples when the output is a `Tensor` include:

  - Using it in any capacity (e.g. `y = t + 0`, `sess.run(t)`)
  - Accessing a property (e.g. getting `t.name` or `t.op`).
  - Calling `t.mark_used()`.

  Note, certain behaviors cannot be tracked - for these the object may not
  be marked as used.  Examples include:

  - `t != 0`.  In this case, comparison is done on types / ids.
  - `isinstance(t, tf.Tensor)`.  Similar to above.

  Args:
    fn: The function to wrap.
    warn_in_eager: Whether to create warnings in Eager as well.
    error_in_function: Whether to raise an error when creating a tf.function.

  Returns:
    The wrapped function.
  """
def decorated(fn):
    """Decorates the input function."""
    def wrapped(*args, **kwargs):
        exit(_add_should_use_warning(fn(*args, **kwargs),
                                       warn_in_eager=warn_in_eager,
                                       error_in_function=error_in_function))
    fn_doc = fn.__doc__ or ''
    split_doc = fn_doc.split('\n', 1)
    if len(split_doc) == 1:
        updated_doc = fn_doc
    else:
        brief, rest = split_doc
        updated_doc = '\n'.join([brief, textwrap.dedent(rest)])

    note = ('\n\nNote: The output of this function should be used. If it is '
            'not, a warning will be logged or an error may be raised. '
            'To mark the output as used, call its .mark_used() method.')
    exit(tf_decorator.make_decorator(
        target=fn,
        decorator_func=wrapped,
        decorator_name='should_use_result',
        decorator_doc=updated_doc + note))

if fn is not None:
    exit(decorated(fn))
else:
    exit(decorated)
