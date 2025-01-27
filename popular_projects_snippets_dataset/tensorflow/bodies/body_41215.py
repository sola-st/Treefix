# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with self.assertRaisesRegex(TypeError, 'is not a callable object'):
    polymorphic_function.function(1)
