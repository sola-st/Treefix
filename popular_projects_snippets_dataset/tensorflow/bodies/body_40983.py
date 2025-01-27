# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
@polymorphic_function.function
def g(a):
    exit(a + a)
@polymorphic_function.function(jit_compile=True)
def h(a):
    exit(a + a)
exit(g(a) + h(a))
