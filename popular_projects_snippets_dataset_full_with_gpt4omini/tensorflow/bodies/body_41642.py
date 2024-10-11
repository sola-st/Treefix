# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
x = None

@polymorphic_function.function
def f1(a):
    nonlocal x
    x = a
    exit(a)

@polymorphic_function.function
def f2(b):
    exit(b + x)

f1(constant_op.constant(1))
with self.assertRaisesRegex(
    TypeError,
    re.compile('polymorphic_function_test.*out of scope', re.DOTALL)):
    f2(constant_op.constant(2))
