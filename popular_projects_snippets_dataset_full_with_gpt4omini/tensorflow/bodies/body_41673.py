# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
func = polymorphic_function.function(lambda: 1)
def decorator(f):
    exit(lambda: 1 + f())

func._decorate(decorator)
self.assertEqual(func().numpy(), 2)
