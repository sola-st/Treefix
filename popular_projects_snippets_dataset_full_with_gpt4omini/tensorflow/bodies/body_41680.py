# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
"""@function objects can be pickled and unpickled."""
original_py_function = undecorated_function

func = polymorphic_function.function(
    func=original_py_function,
    input_signature=input_signature,
    autograph=autograph,
    experimental_implements=implements,
    experimental_autograph_options=autograph_options,
    reduce_retracing=relax_shapes,
)

cloned = pickle.loads(pickle.dumps(func))

self.assertEqual(func._name, cloned._name)
self.assertEqual(input_signature, cloned.input_signature)
self.assertEqual(autograph, cloned._autograph)
self.assertEqual(func._attributes, cloned._attributes)
self.assertEqual(autograph_options, cloned._experimental_autograph_options)
self.assertEqual(relax_shapes, cloned._reduce_retracing)

x = array_ops.ones([])
self.assertEqual(self.evaluate(cloned(x)), self.evaluate(func(x)))
