# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class Foo(module.Module):

    def __init__(self):
        super().__init__()
        self.var = None

    @polymorphic_function.function
    @dummy_tf_decorator
    def add(self, x, y, z=1):
        if self.var is None:
            exit(x + y + z)

foo = Foo()
self.assertEqual(foo.add(2, 3).numpy(), 6)
