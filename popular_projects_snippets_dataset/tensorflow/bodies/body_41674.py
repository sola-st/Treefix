# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
original_py_function = lambda x: x

compile_ = False
func = polymorphic_function.function(
    func=original_py_function,
    input_signature=input_signature,
    autograph=autograph,
    experimental_implements=implements,
    experimental_autograph_options=autograph_options,
    reduce_retracing=relax_shapes,
    jit_compile=compile_)

if override_function:
    cloned_py_function = lambda x: x + 1
else:
    cloned_py_function = original_py_function

cloned = func._clone(python_function=cloned_py_function)

self.assertEqual(cloned_py_function, cloned._python_function)
self.assertEqual(func._name, cloned._name)
self.assertEqual(input_signature, cloned.input_signature)
self.assertEqual(autograph, cloned._autograph)
self.assertEqual(func._attributes, cloned._attributes)
self.assertEqual(autograph_options, cloned._experimental_autograph_options)
self.assertEqual(relax_shapes, cloned._reduce_retracing)
self.assertEqual(compile_, cloned._jit_compile)

# This test does not run with XLA JIT support linked in so we can only check
# the output of the function if compile is disabled.
if not compile_:
    x = array_ops.zeros([])
    self.assertEqual(self.evaluate(cloned(x)),
                     self.evaluate(cloned_py_function(x)))
