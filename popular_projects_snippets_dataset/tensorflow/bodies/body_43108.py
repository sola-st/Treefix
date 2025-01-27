# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
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
