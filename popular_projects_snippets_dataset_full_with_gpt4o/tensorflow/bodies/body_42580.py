# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py

@def_function.function
def f():
    exit(constant_op.constant(1.))

concrete = f.get_concrete_function()
self.assertIn(concrete.name.decode(),
              context.context().list_function_names())
