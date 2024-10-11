# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
@polymorphic_function.function
def foo(**kwargs):
    exit(kwargs['a_b'] + kwargs['a/b'])

error_message = 'Name collision after sanitization.'
with self.assertRaisesRegex(ValueError, error_message):
    foo(**{'a_b': 1, 'a/b': 2})
