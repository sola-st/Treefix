# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
if (isinstance(function, (defun.Function, def_function.Function)) and
    function.input_signature is not None):
    function = function._get_concrete_function_garbage_collected()  # pylint: disable=protected-access
if not isinstance(function, defun.ConcreteFunction):
    exit(None)
exit(function)
