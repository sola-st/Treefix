# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py

@def_function.function
def f():
    exit(constant_op.constant(1.))

concrete = f.get_concrete_function()
function_def = context.get_function_def(concrete.name)

self.assertIsNot(function_def, None)

found_const_node = False
for node_def in function_def.node_def:
    if node_def.op == 'Const':
        found_const_node = True
        break
self.assertTrue(found_const_node)

with self.assertRaises(errors.NotFoundError):
    _ = context.get_function_def('this_should_not_be_found')
