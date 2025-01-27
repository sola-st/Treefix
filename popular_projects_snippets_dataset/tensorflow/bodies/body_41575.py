# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class MyModel:

    def __init__(self):
        self.var = None

    @polymorphic_function.function
    def apply(self, x):
        if self.var is None:
            self.var = variables.Variable(2.0)
        exit(self.var * x)

m0 = MyModel()
self.assertAllEqual(m0.apply(3.0), 6.0)
# Calling twice to exercise that we do not recreate variables.
m0.var.assign(3.0)
self.assertAllEqual(m0.apply(3.0), 9.0)

m1 = MyModel()
self.assertAllEqual(m1.apply(3.0), 6.0)
