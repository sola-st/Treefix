# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
"""Get the object that `self` keyword refers to within a function.

  Args:
    fn: A python function object

  Returns:
    A class object that `self` refers to. Return None if not found.

  Here is an example demonstrating how this helper function works.

  ```
  class Foo():

    def __init__(self):
      self.val = 1

    def bar(self):
      x = 2

      def fn():
        return self.val + x

      return fn

  foo = Foo()
  fn = foo.bar()
  self_obj = _get_self_obj_from_closure(fn)
  assert self_obj is foo
  ```

  The goal is to get the `self_obj` (foo) from `fn`, so that it's feasible to
  access attributes of `foo`, like self.val in this case.

  This function first parses fn.qual_name, "Foo.bar.<locals>.fn", and finds the
  closure whose class name appear in fn.qual_name first.
  """
assert hasattr(fn, "__closure__")
qual_name = fn.__qualname__.split(".")
# Search from the right to left
qual_name = qual_name[::-1]

if fn.__closure__:
    for cls_name in qual_name:
        for cell in fn.__closure__:
            try:
                closure = cell.cell_contents
            except ValueError:
                # Continue when cell is empty and its content is unavailable
                continue
            if inspect.isclass(type(closure)):
                if type(closure).__name__ == cls_name:
                    obj = closure
                    exit(obj)

exit(None)
