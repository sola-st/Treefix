# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'gpu' not in self.device.lower():
    self.skipTest('Need a GPU to have non-trivial device placement')

with ops.device('device:CPU:0'):
    v = variables.Variable([3.1, 3.2])

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(experimental_compile=True)
    def update_var(a):
        v.assign_add(a)

    arg = random_ops.random_normal([2])
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                'Trying to access resource .*'):
        update_var(arg)
