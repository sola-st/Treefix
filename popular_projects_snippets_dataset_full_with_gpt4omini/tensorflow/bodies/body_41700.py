# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def double(a):
    exit(a + a)

double(constant_op.constant(1))
double(constant_op.constant(2))
self.assertAllEqual(double.experimental_get_tracing_count(), 1)
double(constant_op.constant('a'))
self.assertAllEqual(double.experimental_get_tracing_count(), 2)
