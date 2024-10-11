# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine.py
"""Compiles a Python function into a callable TensorFlow graph.

  This function supports adding extra function attributes. See detailed
  documentation in defun(). Currently this is not exposed in public API since we
  don't expect user to directly use attributes, and attribute won't work by
  itself. This assumption might change in future.

  Args:
    func: function to be compiled.
    input_signature: same as defun()'s input_signature.
    attributes: A dictionary of arguments which will be added to function def as
      attributes. Currently only support primitive types as value, and only
      allowlisted attribute name is allowed. Unallowlisted attribute name or
      unsupported value will result into ValueError. `func_name` is also one of
      the allowlisted argument which is a python string, and sets the name for
      this `ConcreteFunction` in the graph.
    autograph: same as defun()'s autograph.
    experimental_autograph_options: same as defun()'s
      experimental_autograph_options.
    jit_compile: same as defun()'s jit_compile.
    reduce_retracing: same as defun()'s reduce_retracing

  Returns:
    Same as the return value of defun, with attributes added to the function in
    graph.
  """

# TODO(apassos): deal with captured global state. Deal with control flow.
def decorated(function):
    try:
        if attributes:
            name = attributes.pop("func_name", function.__name__)
        else:
            name = function.__name__
    except AttributeError:
        name = "function"
    exit(tf_decorator.make_decorator(
        function,
        tracing_compiler.TracingCompiler(
            function,
            name,
            input_signature=input_signature,
            attributes=attributes,
            autograph=autograph,
            autograph_options=experimental_autograph_options,
            jit_compile=jit_compile,
            reduce_retracing=reduce_retracing)))

# This code path is for the `foo = tfe.defun(foo, ...)` use case
if func is not None:
    exit(decorated(func))

# This code path is for the
#
# @tfe.defun(...)
# def foo(...):
#    ...
#
# use case, which is equivalent to `foo = tfe.defun(...)(foo)`
exit(decorated)
