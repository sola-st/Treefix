# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
ctx = context.context()
self.assertFalse(ctx.has_function("not_a_function"))

@def_function.function
def f():
    exit(1.)

self.assertTrue(ctx.has_function(f.get_concrete_function().name))
