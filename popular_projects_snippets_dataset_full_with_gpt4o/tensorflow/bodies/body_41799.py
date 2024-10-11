# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Allows the captured Python function to be decorated in place.

    This method is only safe to call when the Function has not been called by a
    user. It makes sense to use this method to push a decorator into the
    function rather than wrapping the function in the decorator.

    We use this in tf.Module to allow user annotated `tf.functions` to remain as
    `Function` objects but still automatically enter the Module name_scope
    when they are evaluated like all other methods.

    Args:
      decorator: A callable accepting a single argument which is the function
        to decorate and returning a callable result.

    Raises:
      ValueError: If the function has been called a ValueError is raised.
    """
if self._variable_creation_fn is not None or self._no_variable_creation_fn is not None:
    raise ValueError(
        "Functions cannot be decorated after they have been traced.")

self._python_function = decorator(self._python_function)
self._function_spec = function_spec_lib.FunctionSpec.from_function_and_signature(
    self._python_function, self.input_signature)
