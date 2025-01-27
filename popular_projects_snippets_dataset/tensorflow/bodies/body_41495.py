# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
"""Tests for errors in the flat signature.

    Args:
      conc_args: Positional arguments used for get_concrete_function.
      conc_kwargs: Keyword arguments used for get_concrete_function.
      call_args: Positional arguments used to call the function.
      call_kwargs: Keyword arguments used to call the function.
      error: Expected exception message.
      exception: Expected exception type.
    """
conc_args = conc_args() if callable(conc_args) else conc_args
conc_kwargs = conc_kwargs() if callable(conc_kwargs) else conc_kwargs or {}
call_args = call_args() if callable(call_args) else call_args
call_kwargs = call_kwargs() if callable(call_kwargs) else call_kwargs or {}
self.assertIsInstance(conc_args, tuple)
self.assertIsInstance(call_args, tuple)
self.assertIsInstance(conc_kwargs, dict)
self.assertIsInstance(call_kwargs, dict)

@polymorphic_function.function
def func(x, y=5, *varargs, **kwargs):  # pylint: disable=keyword-arg-before-vararg
    del y, varargs, kwargs
    exit(x)

conc = func.get_concrete_function(*conc_args, **conc_kwargs)

# Remove _function_spec, to disable the structured signature.
conc._set_function_spec(None)  # pylint: disable=protected-access

with self.assertRaisesRegex(exception, error):
    self.evaluate(conc(*call_args, **call_kwargs))
