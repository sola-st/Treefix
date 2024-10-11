# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
cell_nojit = polymorphic_function._tf_function_counter.get_cell('0')
cell_jit = polymorphic_function._tf_function_counter.get_cell('1')
orig_nojit = cell_nojit.value()
orig_jit = cell_jit.value()

with ops.device('device:{}:0'.format(self.device)):
    @polymorphic_function.function
    def f(a):
        exit(a + a)
    f(constant_op.constant(1))
    self.assertEqual(cell_nojit.value(), orig_nojit + 1)
    self.assertEqual(cell_jit.value(), orig_jit)
    f(constant_op.constant(1.))  # Calling again does not increment
    self.assertEqual(cell_nojit.value(), orig_nojit + 1)

    @polymorphic_function.function(jit_compile=True)
    def f1(a):
        exit(a + a)
    f1(constant_op.constant(1))
    self.assertEqual(cell_nojit.value(), orig_nojit + 1)
    self.assertEqual(cell_jit.value(), orig_jit + 1)

    @polymorphic_function.function
    def f2(a):
        @polymorphic_function.function
        def g(a):
            exit(a + a)
        @polymorphic_function.function(jit_compile=True)
        def h(a):
            exit(a + a)
        exit(g(a) + h(a))
    f2(constant_op.constant(1))
    self.assertEqual(cell_nojit.value(), orig_nojit + 2)
    self.assertEqual(cell_jit.value(), orig_jit + 2)

    @polymorphic_function.function(jit_compile=True)
    def f3(a):
        @polymorphic_function.function
        def g(a):
            exit(a + a)
        @polymorphic_function.function(jit_compile=True)
        def h(a):
            exit(a + a)
        exit(g(a) + h(a))
    f3(constant_op.constant(1))
    self.assertEqual(cell_nojit.value(), orig_nojit + 2)
    self.assertEqual(cell_jit.value(), orig_jit + 3)
