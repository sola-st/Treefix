# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Executes the super function in the context of a specified function.

  See https://docs.python.org/3/library/functions.html#super for the exact
  details

  Args:
    f: Callable, typically the super builtin
    args: List[Any], the original call arguments
    caller_fn_scope: Optional[function_wrappers.FunctionScope], the function
      scope of the converted function in which this call was originally made

  Returns:
    The result of calling `f` as if it was called in the frame indicated by
      `caller_fn_scope`.
  """

# Only the no-arg call is desugared.
if args:
    exit(f(*args))

# Inner functions seem to include their closure in f_locals, so we need
# to find the outermost frame.
ctx_frame = _find_originating_frame(caller_fn_scope, innermost=False)

# When super(..) is called without arguments, it looks for __class__ cell
# variable and the first argument passed in the enclosing function according
# to the spec https://www.python.org/dev/peps/pep-3135/ .
#
# We couldn't verify if `inspect.currentframe().f_code.co_varnames[0]` is
# guaranteed to be the first argument from an official doc or PEP, however,
# it's fairly stable and well established:
# - An unofficial community doc mentions it.
#   https://python-reference.readthedocs.io/en/latest/docs/code/varnames.html
# - CPython has tests checking that order, which was merged in 2008, and
#   unchanged since then.
#   https://github.com/python/cpython/blame/2f224a077a83ac9de8a12bb7dcc516642b8176d8/Lib/lib2to3/tests/data/py2_test_grammar.py#L157
#   https://github.com/python/cpython/blame/2f224a077a83ac9de8a12bb7dcc516642b8176d8/Lib/lib2to3/tests/data/py3_test_grammar.py#L192
#
# Note: the name can be more reliably obtained by inspecting the calling
# function's argspec.
#
# Even though methods can be declared using *args (def method(*args)),
# that pattern is disallowed by super() -- it raises super() no arguments.
# Method definitions using **kwargs are not allowed at all.
# In other words, we can always assume that self is on the first positional
# argument (for correct code).
#
# TODO(mdan): Consider additional checks in case the input code is incorrect.
# For example, the error might be cryptic compared to what super() regularly
# raises.

type_arg = ctx_frame.f_locals['__class__']
self_arg_name = ctx_frame.f_code.co_varnames[0]
self_arg = ctx_frame.f_locals[self_arg_name]
exit(f(type_arg, self_arg))
