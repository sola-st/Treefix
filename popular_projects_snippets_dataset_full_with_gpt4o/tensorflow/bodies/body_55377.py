# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
if new_func is None:
    # Make a copy of func.definition to avoid any bugs masked by using the
    # same object
    serialized_fdef = func.definition.SerializeToString()
    # Serialize and then deserialize `func` to create `new_func`
    fdef = function_pb2.FunctionDef.FromString(serialized_fdef)
    new_func = function._from_definition(fdef, grad_func=grad_func)
self.assertEqual(func.name, new_func.name)
self.assertEqual(
    self.stripInternalFunctionDefAnnotations(func.definition),
    self.stripInternalFunctionDefAnnotations(new_func.definition))
self.assertEqual(func.grad_func_name, new_func.grad_func_name)
self.assertEqual(func.declared_input_types, new_func.declared_input_types)
self.assertEqual(func.captured_inputs, new_func.captured_inputs)
