# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'tpu' in self.device.lower():
    self.skipTest('Autoclustering does not run on TPU')

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=False)
    def outer(a, b, c):
        exit(a * inner(b, c) + c)

    @polymorphic_function.function(jit_compile=True)
    def inner(b, c):
        exit(b + c * b)

    i1 = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0])
    i2 = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0])
    i3 = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0])

    with context.collect_graphs(optimized=True) as graphs:
        outer(i1, i2, i3)

    if test_util.is_xla_enabled():
        self.assertIn('_XlaRun', [n.op for n in graphs[0].node])
    else:
        self.assertNotIn('_XlaRun', [n.op for n in graphs[0].node])
