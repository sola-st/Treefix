# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
c = constant_op.constant(10, dtypes.int64)

@function.Defun(dtypes.int64)
def Foo(x):
    exit(x + c)

new_func = function._from_definition(Foo.definition)

self.assertEqual(Foo.name, new_func.name)
self.assertEqual(
    self.stripInternalFunctionDefAnnotations(Foo.definition),
    self.stripInternalFunctionDefAnnotations(new_func.definition))
self.assertEqual(Foo.grad_func_name, new_func.grad_func_name)

# Captured inputs are added as regular inputs to the function definition
self.assertEqual(new_func.declared_input_types,
                 Foo.declared_input_types + (dtypes.int64,))
self.assertEqual(len(new_func.captured_inputs), 0)
