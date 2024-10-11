# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
# The single FunctionDef should have one argument, a captured variable
function_def, = graph_def.library.function
self.assertLen(function_def.signature.input_arg, 1)
function_arg, = function_def.signature.input_arg
self.assertEqual(dtypes.resource, dtypes.as_dtype(function_arg.type))
