# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
"""Asserts that native_data matches compiled_data."""
native_results, native_out, native_err = native_data
compiled_results, compiled_out, compiled_err = compiled_data
str_args = '(%s)' % ', '.join(str(a) for a in args)
# Using a manual verification to avoid a second compilation on success.
# For exceptions, we don't enforce that they are the same, only that
# both paths raised.
# TODO(mdan): Add an API that returns both object and source code instead.
outputs_equal = (
    self._deep_equal(native_results, compiled_results) and
    native_out == compiled_out)
errors_equivalent = type(native_err) == type(compiled_err)  # pylint:disable=unidiomatic-typecheck
if (not outputs_equal or not errors_equivalent):
    self.fail('Native and compiled functions are not equivalent.\n\n'
              'Native results: %s\n'
              'Compiled results: %s\n'
              'Native out: %s\n'
              'Compiled out: %s\n'
              'Native error: %s: %s\n'
              'Compiled error: %s: %s\n'
              'Native call: %s%s\n'
              'Check the logs for the generated code.'
              '' % (
                  native_results,
                  compiled_results,
                  native_out,
                  compiled_out,
                  type(native_err).__name__,
                  native_err,
                  type(compiled_err).__name__,
                  compiled_err,
                  f.__name__,
                  str_args,
              ))
