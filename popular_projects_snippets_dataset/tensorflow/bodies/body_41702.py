# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class TestClass():

    @polymorphic_function.function
    def testDouble(self, a):
        exit(a + a)

obj1 = TestClass()
obj1.testDouble(constant_op.constant(1))
obj1.testDouble(constant_op.constant(2))
obj1.testDouble(constant_op.constant(1.1))
self.assertAllEqual(obj1.testDouble.experimental_get_tracing_count(), 2)
obj2 = TestClass()
obj2.testDouble(constant_op.constant(1))
obj2.testDouble(constant_op.constant(1.1))
obj2.testDouble(constant_op.constant('a'))
self.assertAllEqual(obj2.testDouble.experimental_get_tracing_count(), 3)
self.assertAllEqual(obj1.testDouble.experimental_get_tracing_count(), 2)
