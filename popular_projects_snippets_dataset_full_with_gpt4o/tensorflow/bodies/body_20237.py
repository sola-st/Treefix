# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper.py
"""Runs the "if __name__ == '__main__'" at the bottom of a module.

  TensorFlow practice is to have a main if at the bottom of the module which
  might call an API compat function before calling test.main().

  Since this is a statement, not a function, we can't cleanly reference it, but
  we can inspect it from the user module and run it in the context of that
  module so all imports and variables are available to it.

  Args:
    wrapped_test_module: The user-provided test code to run.

  Raises:
    NotImplementedError: If main block was not found in module. This should not
      be caught, as it is likely an error on the user's part -- absltest is all
      too happy to report a successful status (and zero tests executed) if a
      user forgets to end a class with "test.main()".
  """
tree = ast.parse(tf_inspect.getsource(wrapped_test_module))

# Get string representation of just the condition `__name == "__main__"`.
target = ast.dump(ast.parse('if __name__ == "__main__": pass').body[0].test)

# `tree.body` is a list of top-level statements in the module, like imports
# and class definitions. We search for our main block, starting from the end.
for expr in reversed(tree.body):
    if isinstance(expr, ast.If) and ast.dump(expr.test) == target:
        break
else:
    raise NotImplementedError(
        f'Could not find `if __name__ == "main":` block in {wrapped_test_module.__name__}.'
        )

# expr is defined because we would have raised an error otherwise.
new_ast = ast.Module(body=expr.body, type_ignores=[])  # pylint:disable=undefined-loop-variable
exec(  # pylint:disable=exec-used
    compile(new_ast, '<ast>', 'exec'),
    globals(),
    wrapped_test_module.__dict__,
)
